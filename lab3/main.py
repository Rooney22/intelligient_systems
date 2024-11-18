from lab3.Classes.LiftLexer import LiftLexer
from lab3.Classes.LiftState import LiftState

env_state = [(1, 5), (4, 1), (3, 2), (3, 4)]
lexer = LiftLexer(env_state)
lift_state_1 = LiftState('S', [4, []], lexer)
lift_state_2 = LiftState('S', [1, []], lexer)
while not(lift_state_1.state_name == 'E' and lift_state_2.state_name == 'E'):
    lift_state_1.Next()
    lift_state_2.Next()

