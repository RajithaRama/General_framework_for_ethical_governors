from final_evaluator import evaluator


class UtilitarianEvaluator(evaluator.Evaluator):

    def __init__(self):
        super().__init__()

    def evaluate(self, data, logger):
        for action in data.get_actions():
            desirability = 0
            if data.get_table_data(action, 'is_rule_broken'):
                desirability = data.get_table_data(action, "stakeholder_wellbeing") + data.get_table_data(action, 'social') + data.get_table_data(action, 'driver_autonomy')
            else:
                desirability = 2 * data.get_table_data(action, "stakeholder_wellbeing") + data.get_table_data(action, 'social') + 0.75 * data.get_table_data(action, 'driver_autonomy')
            self.score[action] = desirability