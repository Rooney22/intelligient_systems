import numpy as np
from lab3.AbstractClasses.Lexer import Lexer


class LiftLexer(Lexer):
    def __init__(self, env_state):
        self.env_state = env_state

    def get_next_state(self, lift_state, state_name):
        end_dict = {
            True: self.generate_end_command,
            False: self.generate_command,
        }
        return end_dict[len(lift_state[1]) == 0 and len(self.env_state) == 0](lift_state, state_name)

    def generate_end_command(self, lift_state, state_name):
        return lift_state, 'E'

    def generate_command(self, lift_state, state_name):
        doors_dict = {
            True: self.open_doors,
            False: self.check_go,
        }
        doors_condition = self.check_door_condition(lift_state, state_name)
        lift_state, command = doors_dict[doors_condition](lift_state, state_name)
        return lift_state, command

    def find_nearest_out(self, lift_state):
        return min(self.env_state, key=lambda x: abs(x[0] - lift_state[0]))[0]

    def find_nearest_in(self, lift_state):
        return min(lift_state[1], key=lambda x: abs(x - lift_state[0]))

    def open_doors(self, lift_state, state_name):
        lift_state[1] = list(filter(lambda pas: pas != lift_state[0], lift_state[1]))
        passengers_on_floor = list(filter(lambda pas: pas[0] == lift_state[0], self.env_state))
        for pas in passengers_on_floor:
            lift_state[1].append(pas[1])
        self.env_state = list(filter(lambda pas: pas[0] != lift_state[0], self.env_state))
        return lift_state, 'O'

    def check_go(self, lift_state, state_name):
        lift_dict = {
                True: self.find_nearest_out,
                False: self.find_nearest_in,
        }
        nearest = lift_dict[len(lift_state[1]) == 0](lift_state)
        lift_state, command = self.lift_go(lift_state, nearest)
        return lift_state, command

    def lift_go(self, lift_state, nearest):
        dir_dict = {
            True: ['D', -1],
            False: ['U', 1],
        }
        direction_condition = (lift_state[0] - nearest) > 0
        dir_char, dir_step = dir_dict[direction_condition]
        lift_state[0] += dir_step
        return lift_state, dir_char

    def check_door_condition(self, lift_state, state_name):
        dir_dict = {
            'D': -1,
            'U': 1,
        }
        dir = dir_dict[state_name]
        pas_inside_cond = min(lift_state[1], key=lambda x: abs(x - lift_state[0])) == lift_state[0]
        pas_outside = np.where(np.array(self.env_state)[:, 0] - lift_state[0] == 0)
        pas_outside_cond = any(np.where(np.array(self.env_state)[pas_outside][:, 1] - lift_state[0] > 0, 1, -1) == dir)
        return pas_inside_cond or pas_outside_cond
