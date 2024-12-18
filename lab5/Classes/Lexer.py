from collections import deque
import re


class Lexer:

    def __init__(self):
        self.state_dict = dict()
        self.info_dict = dict()
        self.symbols = deque()
        self.current_symbol = ""
        self.non_terminal_symbols = list()

    def initiate_states(self, state_dict):
        self.state_dict = state_dict

    def initiate_info(self, info_dict, non_terminal_symbols):
        self.info_dict = info_dict
        self.non_terminal_symbols = list(non_terminal_symbols)

    def get_symbols(self, text):
        cleaned_text = re.sub(r'\s+', ' ', text)
        raw_symbols = cleaned_text.split()
        for symbol in raw_symbols:
            self.symbols.append(self.__preprocess_symbol(symbol))
        self.symbols.append('-|')
        self.current_symbol = self.symbols.popleft()

    def get_info(self, rule):
        return self.info_dict[rule]

    def action_r(self, rule):
        n, symbol = self.info_dict[rule]
        self.symbols.appendleft(self.current_symbol)
        self.current_symbol = symbol

    def action_s(self):
        self.current_symbol = self.symbols.popleft()

    def get_next_state(self, state_name):
        return self.state_dict[state_name][self.current_symbol].get_action()

    @staticmethod
    def __preprocess_symbol(symbol):
        patterns = {
            'число': r'-?\d+',
            'булеан': r'(True|False)',
            'тип': r'^(int|boolean)',
            'return': r'return',
            'def': r'def',
            'id': r'[a-zA-Z]+',
        }

        for group, pattern in patterns.items():
            if re.match(pattern, symbol):
                return group
        return symbol
