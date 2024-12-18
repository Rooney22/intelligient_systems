from lab5.AbstractClasses.State import State
from lab5.Utility.util import stack


class StateLR(State):

    def __init__(self, lexer):
        self.state_name = '0'
        stack.append('0')
        self.lexer = lexer
        self.logs = []

    def next(self):
        action, number = self.lexer.get_next_state(self.state_name)
        self.logs.append([action, number])
        self.do_action(action, number)

    def do_action(self, action, number):
        action_dict = {
            'R': self.action_r,
            'S': self.action_s,
            'ACC': self.action_acc,
        }
        action_dict[action](number)

    def action_r(self, number):
        n, symbol = self.lexer.get_info(number)
        for i in range(n):
            stack.pop()
        self.state_name = stack.pop()
        stack.append(self.state_name)
        self.lexer.action_r(number)

    def action_s(self, number):
        self.state_name = number
        stack.append(number)
        self.lexer.action_s()

    def action_acc(self, number):
        n, symbol = self.lexer.get_info(number)
        for i in range(n - 1):
            stack.pop()
        self.state_name = 'END'
        self.lexer.action_r(number)
