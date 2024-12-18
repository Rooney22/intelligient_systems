import pandas as pd
import numpy as np
from lab5.Classes.ActionR import ActionR
from lab5.Classes.ActionS import ActionS
from lab5.Classes.ActionAcc import ActionAcc


class TableParser:
    def __init__(self, lexer):
        self.lexer = lexer

    def parse_main_table(self, table_path):
        state_dict = dict()
        table = pd.read_excel(table_path)
        for index, row in table.iterrows():
            state_dict[row['state']] = dict()
            for column in table.columns[1:]:
                if row[column] is np.nan:
                    continue
                if row[column][0] == 'r':
                    state_dict[row['state']][column] = ActionR(row[column][1:])
                elif row[column][0] == 's':
                    state_dict[row['state']][column] = ActionS(row[column][1:])
                elif row[column][0] == 'acc':
                    state_dict[row['state']][column] = ActionAcc(0)
        self.lexer.initiate_states(state_dict)

    def parse_info_table(self, table_path):
        info_dict = dict()
        table = pd.read_excel(table_path, dtype={'State': str, 'NextState': str})
        for index, row in table.iterrows():
            info_dict[row['rule']] = [row['n'], row['return']]
        self.lexer.initiate_info(info_dict)
