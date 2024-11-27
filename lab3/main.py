from lab3.Classes.LiftLexer import LiftLexer
from lab3.Classes.LiftState import LiftState

if __name__ == "__main__":
    env_state = []
    with open('example_input.txt', 'r') as file:
        n_floors = int(file.readline())
        start_floor_1, start_floor_2 = map(int, file.readline().split(' '))
        env_states = file.readline().split(' ')
        for pas_state in env_states:
            pas_state_1, pas_state_2 = map(int, pas_state.split(','))
            env_state.append((pas_state_1, pas_state_2))

    lexer = LiftLexer(env_state)
    lift_state_1 = LiftState([start_floor_1, [], False], lexer)
    lift_state_2 = LiftState([start_floor_2, [], False], lexer)
    while not(lift_state_1.state_name == 'END' and lift_state_2.state_name == 'END'):
        lift_state_1.Next()
        lift_state_2.Next()

    with open('example_output.txt', 'w') as file:
        file.write('Логи лифта 1: \n')
        for log in lift_state_1.logs:
            file.write(log + '\n')
        file.write('Логи лифта 2: \n')
        for log in lift_state_2.logs:
            file.write(log + '\n')
