import numpy as np
from lab3.AbstractClasses.Lexer import Lexer


class LiftLexer(Lexer):
    def __init__(self, env_state):
        self.env_state = env_state

    def get_next_state(self, lift_state, state_name):
        end_dict = {
            True: self.generate_end_state,
            False: self.generate_state,
        }
        return end_dict[len(lift_state[1]) == 0 and len(self.env_state) == 0](lift_state, state_name)

    def generate_end_state(self, lift_state, state_name):
        return lift_state, 'END'

    def generate_state(self, lift_state, state_name):
        state_dict = {
            'O': self.check_go,
        }
        lift_state, state = state_dict.get(state_name[0], self.check_doors)(lift_state, state_name)
        return lift_state, state

    def check_doors(self, lift_state, state_name):
        doors_dict = {
            True: self.open_doors,
            False: self.check_go,
        }
        doors_condition = self.check_door_condition(lift_state, state_name)
        lift_state, state = doors_dict[doors_condition](lift_state, state_name)
        return lift_state, state

    def open_doors(self, lift_state, state_name):
        check_dict = {
            True: self.open_doors_empty,
            False: self.open_doors_full,
        }
        lift_state[1] = list(filter(lambda pas: pas != lift_state[0], lift_state[1]))
        lift_state, state = check_dict[len(lift_state[1]) == 0](lift_state, state_name)
        return lift_state, state

    def open_doors_empty(self, lift_state, state_name):
        passengers_on_floor = list(filter(lambda pas: pas[0] == lift_state[0], self.env_state))
        for pas in passengers_on_floor:
            lift_state[1].append(pas[1])
        self.env_state = list(filter(lambda pas: pas[0] != lift_state[0], self.env_state))
        check_dict = {
            True: 'E',
            False: 'F',
        }
        empty_char = check_dict[len(lift_state[1]) == 0]
        return lift_state, 'O' + empty_char

    def open_doors_full(self, lift_state, state_name):
        dir_dict = {
            'D': False,
            'U': True,
        }
        direction = dir_dict[state_name[0]]
        passengers_on_floor = list(filter(lambda pas: pas[0] == lift_state[0] and ((pas[1] - pas[0] > 0) == dir), self.env_state))
        for pas in passengers_on_floor:
            lift_state[1].append(pas[1])
        self.env_state = list(filter(lambda pas: not(pas[0] == lift_state[0] and ((pas[1] - pas[0] > 0) == dir)), self.env_state))
        return lift_state, 'OF'


    def check_go(self, lift_state, state_name):
        lift_dict = {
                'E': self.find_nearest_out,
                'F': self.find_nearest_in,
        }
        nearest = lift_dict[state_name[1]](lift_state)
        lift_state, state = self.lift_go(lift_state, state_name, nearest)
        return lift_state, state

    def find_nearest_out(self, lift_state):
        return min(self.env_state, key=lambda x: abs(x[0] - lift_state[0]))[0]

    def find_nearest_in(self, lift_state):
        return min(lift_state[1], key=lambda x: abs(x - lift_state[0]))

    def lift_go(self, lift_state, state_name, nearest):
        dir_dict = {
            True: 'D',
            False: 'U',
        }
        direction_condition = (lift_state[0] - nearest) > 0
        dir_char = dir_dict[direction_condition]
        return lift_state, dir_char + state_name[1]

    def check_door_condition(self, lift_state, state_name):
        empty_dict = {
            'F': self.check_full_door_condition,
            'E': self.check_empty_door_condition,
        }
        return empty_dict[state_name[1]](lift_state, state_name)

    def check_empty_door_condition(self, lift_state, state_name):
        pas_outside_cond = any(np.where(np.array(self.env_state)[:, 0] == lift_state[0], 1, 0) == 1)
        return pas_outside_cond

    def check_full_door_condition(self, lift_state, state_name):
        dir_dict = {
            'D': -1,
            'U': 1,
        }
        dir = dir_dict[state_name[0]]
        pas_inside_cond = min(lift_state[1], key=lambda x: abs(x - lift_state[0])) == lift_state[0]
        pas_outside = np.where(np.array(self.env_state)[:, 0] == lift_state[0])
        pas_outside_cond = any(np.where(np.array(self.env_state)[pas_outside][:, 1] - lift_state[0] > 0, 1, -1) == dir)
        return pas_outside_cond or pas_inside_cond

    def get_action(self, state_name):
        dir_action = {
            'D': 'DOWN',
            'U': 'UP',
            'O': 'OPEN',
        }
        return dir_action.get(state_name[0], 'NONE')

    def get_end_action(self, state_name):
        dir_action = {
            'O': 'CLOSE',
        }
        return dir_action.get(state_name[0], 'NONE')
