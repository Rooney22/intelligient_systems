from lab3.AbstractClasses.Lexer import Lexer


class LiftLexer(Lexer):
    def __init__(self, env_state):
        self.env_state = env_state

    def get_next_state(self, lift_state):
        end_dict = {
            True: self.generate_end_command,
            False: self.generate_command,
        }
        return end_dict[len(lift_state[1]) == 0 and len(self.env_state) == 0](lift_state)

    def generate_end_command(self, lift_state):
        return lift_state, 'E'

    def generate_command(self, lift_state):
        lift_dict = {
                True: self.find_nearest_out,
                False: self.find_nearest_in,
        }
        doors_dict = {
            True: self.open_doors,
            False: self.check_go,
        }
        nearest = lift_dict[len(lift_state[1]) == 0](lift_state)
        lift_state, command = nearest_dict.get(lift_state[0] - nearest, self.lift_go)(lift_state, nearest)
        return lift_state, command

    def find_nearest_out(self, lift_state):
        return min(self.env_state, key=lambda x: abs(x[0] - lift_state[0]))[0]

    def find_nearest_in(self, lift_state):
        return min(lift_state[1], key=lambda x: abs(x - lift_state[0]))

    def open_doors(self, lift_state, nearest):
        lift_state[1] = list(filter(lambda pas: pas != lift_state[0], lift_state[1]))
        passengers_on_floor = list(filter(lambda pas: pas[0] == lift_state[0], self.env_state))
        for pas in passengers_on_floor:
            print(pas)
            lift_state[1].append(pas[1])
        self.env_state = list(filter(lambda pas: pas[0] != lift_state[0], self.env_state))
        return lift_state, 'O'

    def lift_go(self, lift_state, nearest):
        dir_dict = {
            True: ['D', -1],
            False: ['U', 1],
        }
        direction_condition = (lift_state[0] - nearest) > 0
        dir_char, dir_step = dir_dict[direction_condition]
        lift_state[0] += dir_step
        return lift_state, dir_char
