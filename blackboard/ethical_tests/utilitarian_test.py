# To-Do:
import ethical_test


def bar():
    print("bar")


class UtilitarianTest(ethical_test.EthicalTest):

    def __init__(self, test_data):
        super().__init__(test_data)
