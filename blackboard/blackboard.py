import yaml
import importlib
import ethical_tests
import sys
import scheduler
import logging

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

        # Loading logger
        self.process_logger = logging.getLogger('Decision_making_log')
        formatter = logging.Formatter('%(asctime)s - %(module)s - %(message)s')
        file_handler = logging.FileHandler(filename=self.conf.get('log_file', 'Decision_making_log'), mode='w')
        stream_handler = logging.StreamHandler()
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)
        self.process_logger.addHandler(stream_handler)
        self.process_logger.addHandler(file_handler)
        self.process_logger.setLevel(logging.INFO)

        # self.process_logger.

        # Loading test modules
        self.test_modules = {}
        for key in self.conf["tests"].keys():
            self.test_modules[key] = importlib.import_module("ethical_tests." + self.conf["tests"][key]["module_name"])

        # Loading loader module
        self.data_loader_module = importlib.import_module("data_loader." + self.conf["data_loader"]["module_name"])
        data_loader_class = getattr(self.data_loader_module, self.conf["data_loader"]["class_name"])
        self.data_loader = data_loader_class()

        # Loading data
        self.data = data_structure.Data(self.data_loader.load(input_yaml), self.conf)
        self.process_logger.info('Loaded the data to the blackboard.')
        self.data.log_table(self.process_logger)

        # Loading scheduler
        self.scheduler_module = importlib.import_module("scheduler." + self.conf["scheduler"]["module_name"])
        scheduler_class = getattr(self.scheduler_module, self.conf["scheduler"]["class_name"])
        self.scheduler = scheduler_class(self.conf)

        # Loading final_evaluator
        self.evaluator_module = importlib.import_module("final_evaluator." + self.conf["evaluator"]["module_name"])
        evaluator_class = getattr(self.evaluator_module, self.conf["evaluator"]["class_name"])
        self.evaluator = evaluator_class()

    def run_tests(self):
        self.process_logger.info('Starting tests...')
        for test in self.scheduler.next():
            test_class = getattr(self.test_modules[test], self.conf["tests"][test]["class_name"])
            test_i = test_class(self.conf["tests"][test])
            self.process_logger.info('Running ' + test + ' test.')
            test_i.run_test(self.data, self.process_logger)
            results = test_i.get_results()
            for action, values in results.items():
                for column, value in values.items():
                    self.data.put_table_data(action, column, value)
            self.process_logger.info('Blackboard updated with ' + test + ' test results.')
            self.data.log_table(self.process_logger)
        self.process_logger.info('Testing completed.')
        self.data.log_table(self.process_logger)

    def recommend(self):
        # print(self.data._table_df)
        self.process_logger.info('Calling the final evaluator.')
        self.evaluator.evaluate(self.data, self.process_logger)
        results = self.evaluator.get_results()
        for action, score in results.items():
            self.data.put_table_data(action, "score", value=score)

        self.process_logger.info("Evaluation completed.")
        self.data.log_table(self.process_logger)

        recommendation = [i.value for i in self.data.get_max_index("score")]
        self.process_logger.info('Recommended actions: ' + str(recommendation))
        # print(self.data._table_df)
        return recommendation


if __name__ == "__main__":
    # blackboard = Blackboard("../Lying_dilemma.yaml", "lying_dilemma_deontology_conf.yaml")
    # blackboard = Blackboard("../obedience_dilemma.yaml", "obedience_dilemma_utilitarian_conf.yaml")
    blackboard = Blackboard("../speeding_dilemma.yaml", "speeding_dilemma_conf.yaml")
    blackboard.run_tests()
    print(blackboard.recommend())
