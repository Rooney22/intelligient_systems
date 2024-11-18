from ..AbstractClasses.State import State

class LiftState(State):

    def __init__(self, state_name, lift_state, lexer):
        self.state_name = state_name
        self.lexer = lexer
        self.lift_state = lift_state

    def Next(self):
        new_lift_state, next_state = self.lexer.get_next_state(self.lift_state, self.state_name)
        self.state_name = next_state
        self.lift_state = new_lift_state
