from collections import deque
import re


class Lexer:

    def __init__(self):
        self.state_dict = dict()
        self.error_list = list()
        self.symbols_dict = dict()
        self.symbols = deque()
        self.current_symbol = ""

    def initiate(self, state_dict, error_list, symbols_dict):
        self.state_dict = state_dict
        self.error_list = error_list
        self.symbols_dict = symbols_dict

    def get_symbols(self, text):
        cleaned_text = re.sub(r'\s+', ' ', text)
        raw_symbols = cleaned_text.split()
        for symbol in raw_symbols:
            self.symbols.append(self.__preprocess_symbol(symbol))
        self.current_symbol = self.symbols.popleft()

    def error(self, state_num, next_state):
        error_dict = {
            True: self.__check_error_state,
            False: self.__check_no_error_state
        }
        return error_dict[state_num in error_dict](state_num, next_state)

    def accept(self):
        self.current_symbol = self.symbols.popleft()

    def get_next_state(self, next_state):
        return self.state_dict[next_state]

    @staticmethod
    def __preprocess_symbol(symbol):
        patterns = {
            'number': r'-?\d+',
            'boolean': r'(True|False)',
            'type': r'^(int|boolean)',
            'return': r'return',
            'def': r'def',
            'id': r'[a-zA-Z]+',
        }

        for group, pattern in patterns.items():
            if re.match(pattern, symbol):
                return group
        return symbol

    def __check_no_error_state(self, state_num, next_state):
        check_dict = {
            True: next_state,
            False: state_num[:-1] + str(int(state_num[-1]) + 1)
        }
        print(self.current_symbol, self.symbols_dict[state_num])
        return check_dict[self.current_symbol in self.symbols_dict[state_num]]

    def __check_error_state(self, state_num, next_state):
        if self.current_symbol in self.symbols_dict[state_num]:
            return next_state
        raise ValueError("Ошибка направляющего символа")
