import yaml
import importlib
import sys

sys.path.append("ethical_tests")
sys.path.append("final_evaluator")

import data_structure

CONF_FILE = "../conf.yaml"


class Blackboard:

    def __init__(self, input_yaml):
        self.conf = self.load_yaml(CONF_FILE)

        # Loading test modules
        self.test_modules = {}
        for key in self.conf["test_order"]:
            self.test_modules[key] = (importlib.import_module(self.conf["tests"][key]["module_name"],
                                                              package="ethical_tests"))

        # Loading data
        self.data = data_structure.Data(self.load_yaml(input_yaml), self.conf)

        # Loading final_evaluator
        self.evaluator_module = importlib.import_module(self.conf["evaluator"]["module_name"],
                                                        package="final_evaluator")
        evaluator_class = getattr(self.evaluator_module, self.conf["evaluator"]["class_name"])
        self.evaluator = evaluator_class()

        # self.test_modules["Utilitarian"].bar()
        # self.test_modules["Deontology"].foo()

    def run_tests(self, order=None):
        if order is None:
            order = self.conf["test_order"]

        for test in order:
            test_class = getattr(self.test_modules[test], self.conf["tests"][test]["class_name"])
            test_i = test_class(self.conf["tests"][test])
            test_i.run_test(self.data)
            results = test_i.get_results()
            for action, values in results.items():
                for column, value in values.items():
                    self.data.put_table_data(action, column, value)

    def recommend(self):
        self.evaluator.evaluate(self.data)
        results = self.evaluator.get_results()
        for action, score in results.items():
            self.data.put_table_data(action, "score", value=score)

        recommendation = self.data.get_max_index("score")
        return recommendation
        pass

    def load_yaml(self, input_yaml):
        with open(input_yaml, 'r') as fp:
            yaml_data = yaml.load(fp, Loader=yaml.FullLoader)
        return yaml_data


if __name__ == "__main__":
    blackboard = Blackboard("../yaml_test_1.yaml")
    blackboard.run_tests()
    print(blackboard.recommend())
