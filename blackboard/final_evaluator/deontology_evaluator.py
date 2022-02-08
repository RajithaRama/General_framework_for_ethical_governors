import evaluator


class DeontologyEvaluator(evaluator.Evaluator):

    def __init__(self):
        super().__init__()

    def evaluate(self, data):
        print("evaluated")
