from lab5.AbstractClasses.Action import Action


class ActionS(Action):
    def __init__(self, state_number):
        self.state_number = state_number

    def get_action(self):
        return ['S', self.state_number]
