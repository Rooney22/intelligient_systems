from lab5.Classes.Lexer import Lexer
from lab5.Classes.TableParser import TableParser
from lab5.Classes.StateLR import StateLR

def check_file(file_path, output_path):
    with open(file_path, 'r') as file:
        lexer.get_symbols(file.read())
    state = StateLR(lexer)
    try:
        while state.state_name != 'END':
            state.next()
        with open(output_path, 'w') as file:
            file.write('State action logs: \n')
            for log in state.logs:
                file.write(' '.join(log) + '\n')
    except Exception as e:
        with open(output_path, 'w') as file:
            file.write('Wrong sentence')




if __name__ == "__main__":
    table_path = 'my_LL.xlsx'
    lexer = Lexer()
    table_parser = TableParser(lexer)
    table_parser.parse_main_table('my_LR.xlsx')
    table_parser.parse_info_table('rule_info.xlsx')
    check_file('input_example.txt', 'example_output.txt')
    check_file('wrong_example.txt', 'example_output_wrong.txt')
