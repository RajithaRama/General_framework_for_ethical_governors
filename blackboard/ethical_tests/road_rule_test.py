
from ethical_tests import ethical_test
import yaml

def load_yaml(input_yaml):
    with open(input_yaml, 'r') as fp:
        yaml_data = yaml.load(fp, Loader=yaml.FullLoader)
    return yaml_data

class RoadRuleTest(ethical_test.EthicalTest):

    class rule:
        condition = None
        permissibility = None

        operations = {'<': lambda left, right: left < right,
                      '>': lambda left, right: left > right,
                      'and': lambda left, right: left and right,
                      'or': lambda left, right: left or right,
                      '==': lambda left, right: left == right}

        def read_formula(self):
            pass


        def __init__(self, condition, permissibility):
            self.condition = condition
            self.permissibility = permissibility

        def get_action(self):
            return self.condition

        def get_permissibility(self):
            return self.permissibility


    def __init__(self, ):