from lab5.AbstractClasses.Action import Action

class ActionR(Action):
    def __init__(self, rule_number):
        self.rule_number = rule_number

    def get_action(self):
        return ['R', self.rule_number]
