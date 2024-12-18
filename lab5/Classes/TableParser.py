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
            state = str(row['state'])
            state_dict[state] = dict()
            check_dict = {
                'r': self.__add_r_action,
                's': self.__add_s_action,
                'a': self.__add_acc_action
            }
            for column in table.columns[1:]:
                if row[column] is not np.nan:
                    check_dict.get(row[column][0])(state_dict, state, column, row[column][1:])
        self.lexer.initiate_states(state_dict)

    def parse_info_table(self, table_path):
        info_dict = dict()
        table = pd.read_excel(table_path, dtype={'State': str, 'NextState': str})
        for index, row in table.iterrows():
            info_dict[str(row['rule'])] = [row['n'], row['return']]
        self.lexer.initiate_info(info_dict, set(table['return']))
    
    @staticmethod
    def __add_r_action(state_dict, state, column, number):
        state_dict[state][column] = ActionR(number)
    
    @staticmethod
    def __add_s_action(state_dict, state, column, number):
        state_dict[state][column] = ActionS(number)
        
    @staticmethod    
    def __add_acc_action(state_dict, state, column, number):
        state_dict[state][column] = ActionAcc('0')
    
    @staticmethod
    def __none_action(state_dict, state, column, number):
        pass
