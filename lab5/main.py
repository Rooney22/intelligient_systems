from lab5.Classes.Lexer import Lexer
from lab5.Classes.TableParser import TableParser
from lab5.Classes.StateLR import StateLR


def get_error():
    return "Выражение не принадлежит языку"


if __name__ == "__main__":
    table_path = 'my_LL.xlsx'
    lexer = Lexer()
    table_parser = TableParser(lexer)
    table_parser.parse_main_table('my_LR.xlsx')
    table_parser.parse_info_table('rule_info.xlsx')
    with open('input_example.txt', 'r') as file:
        lexer.get_symbols(file.read())
    state = StateLR(lexer)
    while state.state_name != 'END':
        state.next()