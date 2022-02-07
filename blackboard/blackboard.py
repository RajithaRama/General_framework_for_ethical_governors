import yaml
import importlib
import sys

sys.path.append("./ethical_tests")

import data_structure


CONF_FILE = "../conf.yaml"


class Blackboard:

    def __init__(self, input_yaml):
        self.conf = self.load_yaml(CONF_FILE)
        self.test_modules = {}
        for key in self.conf["test_order"]:
            self.test_modules[key] = (importlib.import_module(self.conf["tests"][key]["module_name"],
                                                             package="ethical_tests"))
        self.data = data_structure.Data(self.load_yaml(input_yaml), self.conf)

        self.test_modules["Utilitarian"].bar()
        self.test_modules["Deontology"].foo()

    def load_yaml(self, input_yaml):
        with open(input_yaml, 'r') as fp:
            yaml_data = yaml.load(fp, Loader=yaml.FullLoader)
        return yaml_data


if __name__ == "__main__":
    blackboard = Blackboard("../yaml_test_1.yaml")