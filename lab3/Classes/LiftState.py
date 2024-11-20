from lab3.AbstractClasses.State import State


class LiftState(State):

    def __init__(self, lift_state, lexer):
        self.state_name = 'SE'
        self.lexer = lexer
        self.lift_state = lift_state
        self.logs = []

    def Next(self):
        new_lift_state, next_state = self.lexer.get_next_state(self.lift_state, self.state_name)
        self.lift_state = new_lift_state
        self.do_action(self.lexer.get_action(next_state))
        self.do_action(self.lexer.get_end_action(next_state))
        self.state_name = next_state

    def do_action(self, action):
        action_dict = {
            'UP': self.up_action,
            'DOWN': self.down_action,
            'OPEN': self.open_action,
            'CLOSE': self.close_action,
        }
        action_dict.get(action, self.none_action)()

    def up_action(self):
        self.lift_state[0] += 1
        self.logs.append(f'Лифт поднялся на этаж {self.lift_state[0]}')

    def down_action(self):
        self.lift_state[0] -= 1
        self.logs.append(f'Лифт опустился на этаж {self.lift_state[0]}')

    def open_action(self):
        self.lift_state[2] = True
        self.logs.append('Лифт открыл двери')

    def close_action(self):
        self.lift_state[2] = False
        self.logs.append('Лифт закрыл двери')

    def none_action(self):
        pass
