import pandas as pd
from lab2.Classes.StateR import StateR
from lab2.Classes.StateS import StateS
from lab2.Classes.StateRA import StateRA
from lab2.Classes.StateA import StateA
from lab2.Classes.StateNormal import StateNormal


class TableParser:
    def __init__(self, lexer):
        self.lexer = lexer

    def parse_table(self, table_path):
        variations_dict = {
            '100': StateA,
            '110': StateRA,
            '001': StateS,
            '010': StateR,
            '000': StateNormal,
        }
        state_dict = dict()
        error_list = list()
        symbols_dict = dict()
        table = pd.read_excel(table_path, dtype={'State': str, 'NextState': str})
        for index, row in table.iterrows():
            variation = str(row['Accept']) + str(row['Return']) + str(row['Stack'])
            state_dict[row['State']] = variations_dict[variation](row['State'], row['NextState'], self.lexer)
            symbols_dict[row['State']] = row['Множество направляющих символов'].split(', ')
            if row['Error']:
                error_list.append(row['State'])
        self.lexer.initiate(state_dict, error_list, symbols_dict)
        start_state = next(iter(state_dict.values()))
        return start_state
