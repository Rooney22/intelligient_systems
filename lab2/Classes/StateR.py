from lab2.AbstractClasses.State import State
from lab2.Utility.util import stack


class StateR(State):
    def __init__(self, state_num, next_state, lexer):
        self.state_num = state_num
        self.next_state = next_state
        self.lexer = lexer

    def next(self):
        next_state = self.lexer.error(self.state_num, self.next_state)
        try:
            return self.lexer.get_next_state(stack.pop())
        except IndexError:
            raise ValueError('Стек пустой')
