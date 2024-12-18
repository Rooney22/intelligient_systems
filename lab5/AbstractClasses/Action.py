from abc import ABCMeta, abstractmethod


class Action():
    __metaclass__=ABCMeta

    @abstractmethod
    def get_action(self):
        """Выполнить действие"""
