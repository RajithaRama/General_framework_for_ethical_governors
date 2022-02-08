import pandas as pd


class Data:

    def __init__(self, loaded_yaml, conf):
        self.environment = loaded_yaml['Environment']
        self.actions = loaded_yaml['Suggested_actions']
        self.stakeholders = loaded_yaml['Stakeholders']

        columns = []
        for key in conf["tests"].keys():
            columns.append(conf["tests"][key]["output_names"])
        columns = [item for sublist in columns for item in sublist]
        columns.append('score')

        self.table_df = pd.DataFrame(columns=columns, index=self.actions)
        print(self.table_df)

    def get_environment_data(self):
        return self.environment

    def get_actions(self):
        return self.actions

    def get_stakeholders_data(self):
        return self.stakeholders

    def get_table_data(self, action, column):
        return self.table_df.loc[action, column]

    def put_table_data(self, results):
        for action, values in results.items():
            for column, value in values.items():
                self.table_df.loc[action, column] = value
        return

    def put_table_data(self, action, column, value):
        self.table_df.loc[action, column] = value

    def get_max_index(self, column):
        column_value = self.table_df[column]
        return column_value[column_value == column_value.max()].index.to_list()
