# TO-DO
import ethical_test


def foo():
    print("foo")


class DeontologyTest(ethical_test.EthicalTest):

    def run_test(self, data):
        pass

    def __init__(self, test_data):
        super().__init__(test_data)
