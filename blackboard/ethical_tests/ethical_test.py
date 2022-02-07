
class EthicalTest:
    def __init__(self, test_data):
        self.number_of_outputs = test_data['number_of_outputs']
        self.output_names = test_data['output_names']
        self.output = {}
        for i in range(self.number_of_outputs):
            self.output[self.output_names[i]] = None

    def run_test(self):
        raise NotImplementedError("Please implement this method")
        pass

    def get_results(self):
        raise NotImplementedError("Please implement this method")
        pass

