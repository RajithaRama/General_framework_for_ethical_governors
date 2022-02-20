from final_evaluator import evaluator


class DeontologyEvaluator(evaluator.Evaluator):

    def __init__(self):
        super().__init__()

    def evaluate(self, data):
        for action in data.get_actions():
            if data.get_table_data(action, 'is_breaking_rule'):
                self.score[action] = 0
            else:
                self.score[action] = 1
        print("evaluated")
