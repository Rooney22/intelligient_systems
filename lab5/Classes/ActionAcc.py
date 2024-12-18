from lab5.AbstractClasses.Action import Action


class ActionAcc(Action):
    def __init__(self, rule_number):
        self.rule_number = rule_number

    def get_action(self):
        return ['ACC', self.rule_number]
