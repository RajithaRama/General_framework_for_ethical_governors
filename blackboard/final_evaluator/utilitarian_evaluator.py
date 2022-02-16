from final_evaluator import evaluator


class UtilitarianEvaluator(evaluator.Evaluator):

    def __init__(self):
        super().__init__()

    def evaluate(self, data):
        for action in data.get_actions():
            desirability = 0
            if data.get_table_data(action, "user_safety") == 0:
                desirability = data.get_table_data(action, "obedience") + 0.75 * data.get_table_data(action,
                                                                                                  "robot_safety")
            else:
                desirability = 2 * data.get_table_data(action, "user_safety") + 0.75 * data.get_table_data(action,
                                                                                                           "robot_safety")

            self.score[action] = desirability


        print("evaluated")