from abc import ABCMeta, abstractmethod


class State:
    __metaclass__=ABCMeta

    @abstractmethod
    def next(self):
        """Получить следующее состояние"""
