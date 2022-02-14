import yaml
import importlib
import ethical_tests
import sys
import scheduler

# sys.path.append("ethical_tests")
# sys.path.append("final_evaluator")
# sys.path.append("utility_functions")

import data_structure
from utility_functions import u_func
from scheduler import round_robin_scheduler

CONF_FILE = "../conf.yaml"


class Blackboard:

    def __init__(self, input_yaml, conf=CONF_FILE):
        self.conf = u_func.load_yaml(conf)

        # Loading test modules
        self.test_modules = {}
        for key in self.conf["test_order"]:
            self.test_modules[key] = importlib.import_module("ethical_tests."+ self.conf["tests"][key]["module_name"])

        # Loading data
        self.data = data_structure.Data(u_func.load_yaml(input_yaml), self.conf)

        # Loading final_evaluator
        self.evaluator_module = importlib.import_module("final_evaluator." + self.conf["evaluator"]["module_name"])
        evaluator_class = getattr(self.evaluator_module, self.conf["evaluator"]["class_name"])
        self.evaluator = evaluator_class()

        # self.test_modules["Utilitarian"].bar()
        # self.test_modules["Deontology"].foo()

    def run_tests(self, order=None):
        if order is None:
            order = self.conf["test_order"]

        scheduler = round_robin_scheduler.RoundRobin(conf=self.conf)
        for test in scheduler.next():
            test_class = getattr(self.test_modules[test], self.conf["tests"][test]["class_name"])
            test_i = test_class(self.conf["tests"][test])
            test_i.run_test(self.data)
            results = test_i.get_results()
            for action, values in results.items():
                for column, value in values.items():
                    self.data.put_table_data(action, column, value)

    def recommend(self):
        print(self.data.table_df)
        self.evaluator.evaluate(self.data)
        results = self.evaluator.get_results()
        for action, score in results.items():
            self.data.put_table_data(action, "score", value=score)

        recommendation = self.data.get_max_index("score")
        return recommendation


if __name__ == "__main__":
    blackboard = Blackboard("../Lying_dilemma.yaml", "lying_dilemma_deontology_conf.yaml")
    blackboard.run_tests()
    print(blackboard.recommend())
