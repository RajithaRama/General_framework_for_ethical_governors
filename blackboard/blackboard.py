import yaml
import importlib
import ethical_tests
import sys
import scheduler

# sys.path.append("ethical_tests")
# sys.path.append("final_evaluator")
# sys.path.append("common_utils")

import data_structure
from common_utils import u_func

CONF_FILE = "../conf.yaml"

def load_yaml(input_yaml):
    with open(input_yaml, 'r') as fp:
        yaml_data = yaml.load(fp, Loader=yaml.FullLoader)
    return yaml_data

class Blackboard:

    def __init__(self, input_yaml, conf=CONF_FILE):
        self.conf = load_yaml(conf)

        # Loading test modules
        self.test_modules = {}
        for key in self.conf["test_order"]:
            self.test_modules[key] = importlib.import_module("ethical_tests."+ self.conf["tests"][key]["module_name"])

        # Loading loader module
        self.data_loader_module = importlib.import_module("data_loader." + self.conf["data_loader"]["module_name"])
        data_loader_class = getattr(self.data_loader_module, self.conf["data_loader"]["class_name"])
        self.data_loader = data_loader_class()

        # Loading data
        self.data = data_structure.Data(self.data_loader.load(input_yaml), self.conf)

        # Loading scheduler
        self.scheduler_module = importlib.import_module("scheduler." + self.conf["scheduler"]["module_name"])
        scheduler_class = getattr(self.scheduler_module, self.conf["scheduler"]["class_name"])
        self.scheduler = scheduler_class(self.conf)

        # Loading final_evaluator
        self.evaluator_module = importlib.import_module("final_evaluator." + self.conf["evaluator"]["module_name"])
        evaluator_class = getattr(self.evaluator_module, self.conf["evaluator"]["class_name"])
        self.evaluator = evaluator_class()

        # self.test_modules["Utilitarian"].bar()
        # self.test_modules["Deontology"].foo()

    def run_tests(self):
        for test in self.scheduler.next():
            test_class = getattr(self.test_modules[test], self.conf["tests"][test]["class_name"])
            test_i = test_class(self.conf["tests"][test])
            test_i.run_test(self.data)
            results = test_i.get_results()
            for action, values in results.items():
                for column, value in values.items():
                    self.data.put_table_data(action, column, value)

    def recommend(self):
        print(self.data._table_df)
        self.evaluator.evaluate(self.data)
        results = self.evaluator.get_results()
        for action, score in results.items():
            self.data.put_table_data(action, "score", value=score)

        recommendation = [i.value for i in self.data.get_max_index("score")]
        print(self.data._table_df)
        return recommendation


if __name__ == "__main__":
    # blackboard = Blackboard("../Lying_dilemma.yaml", "lying_dilemma_deontology_conf.yaml")
    # blackboard = Blackboard("../obedience_dilemma.yaml", "obedience_dilemma_utilitarian_conf.yaml")
    blackboard = Blackboard("../speeding_dilemma.yaml", "speeding_dilemma_conf.yaml")
    blackboard.run_tests()
    print(blackboard.recommend())
