import pandas as pd


class Data:

    def __init__(self, loaded_yaml, conf):
        self._environment = loaded_yaml['Environment']
        self._actions = [Action(i) for i in loaded_yaml['Suggested_actions']]
        self._stakeholders = loaded_yaml['Stakeholders']

        self._other_inputs = loaded_yaml['Other_inputs']

        columns = []
        for key in conf["tests"].keys():
            columns.append(conf["tests"][key]["output_names"])
        columns = [item for sublist in columns for item in sublist]
        columns.append('score')

        self._table_df = pd.DataFrame(columns=columns, index=self._actions)
        print(self._table_df)

    def get_environment_data(self):
        return self._environment

    def get_actions(self):
        return self._actions

    def get_stakeholders_data(self):
        return self._stakeholders

    def get_table_data(self, action, column):
        return self._table_df.loc[action, column]

    def get_other_inputs(self):
        return self._other_inputs

    # def put_table_data(self, results):
    #     for action, values in results.items():
    #         for column, value in values.items():
    #             self.table_df.loc[action, column] = value
    #     return

    def put_table_data(self, action, column, value):
        self._table_df.loc[action, column] = value

    def get_max_index(self, column):
        column_value = self._table_df[column]
        return column_value[column_value == column_value.max()].index.to_list()


class Action:
    def __init__(self, action):
        self.value = action

    def __str__(self):
        return "{}".format(self.value)
