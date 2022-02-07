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
