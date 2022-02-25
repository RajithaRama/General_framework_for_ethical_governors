# TO-DO
from ethical_tests import ethical_test
import yaml


# def foo():
#     print("foo")


def load_yaml(input_yaml):
    with open(input_yaml, 'r') as fp:
        yaml_data = yaml.load(fp, Loader=yaml.FullLoader)
    return yaml_data


class ActDeontologyTest(ethical_test.EthicalTest):
    class rule:
        action = None
        permissibility = None

        def __init__(self, action, permissibility):
            self.action = action
            self.permissibility = permissibility

        def get_action(self):
            return self.action

        def get_permissibility(self):
            return self.permissibility

    def __init__(self, test_data):
        super().__init__(test_data)
        self.rules = {}
        for id, action, perm in load_yaml("./ethical_tests/conf/act_deontology_rules.yaml"):
            self.rules[id] = self.rule(action, perm)

    def run_test(self, data, logger):
        for action in data.get_actions():
            permissible = True
            ids_of_broken_rules = []
            for id, rule in self.rules.items():
                if action != rule.get_action():
                    continue
                elif rule.get_permissibility() < 0:
                    permissible = False
                    ids_of_broken_rules.append(id)
            self.output[action] = {self.output_names[0]: not permissible, self.output_names[1]: ids_of_broken_rules}
