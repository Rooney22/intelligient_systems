from lab2.Classes.Lexer import Lexer
from lab2.Classes.TableParser import TableParser


if __name__ == "__main__":
    table_path = 'my_LL.xlsx'
    lexer = Lexer()
    table_parser = TableParser(lexer)
    start_state = table_parser.parse_table('my_LL.xlsx')
    with open('input_example.txt', 'r') as file:
        lexer.get_symbols(file.read())
    state = start_state
    while(True):
        state = state.next()
