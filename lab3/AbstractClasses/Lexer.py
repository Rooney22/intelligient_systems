from abc import ABCMeta, abstractmethod

class Lexer():
    __metaclass__=ABCMeta

    @abstractmethod
    def get_next_state(self, lift_state, state_name):
        """Получить следующее состояние"""
