from lab2.Classes.Lexer import Lexer
from lab2.Classes.TableParser import TableParser


def get_error():
    return "Выражение не принадлежит языку"


if __name__ == "__main__":
    table_path = 'my_LL.xlsx'
    lexer = Lexer()
    table_parser = TableParser(lexer)
    start_state = table_parser.parse_table('my_LL.xlsx')
    with open('input_example.txt', 'r') as file:
        lexer.get_symbols(file.read())
    state = start_state
    error_dict = {
        "Ошибка направляющего символа": get_error,
        "Стек пустой": lexer.check_end,
    }
    while(True):
        try:
            state = state.next()
        except ValueError as e:
            print(error_dict[str(e)]())
            break
