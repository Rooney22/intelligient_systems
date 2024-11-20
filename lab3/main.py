from lab3.Classes.LiftLexer import LiftLexer
from lab3.Classes.LiftState import LiftState


env_state = [(1, 5), (4, 1), (3, 2), (3, 4)]
lexer = LiftLexer(env_state)
lift_state_1 = LiftState('SE', [4, [], False], lexer)
lift_state_2 = LiftState('SE', [1, [], False], lexer)
while not(lift_state_1.state_name == 'END' and lift_state_2.state_name == 'END'):
    lift_state_1.Next()
    print(lift_state_1.lift_state)
    print(lexer.env_state)
    lift_state_2.Next()
    print(lift_state_2.lift_state)
    print(lexer.env_state)
