from abc import ABCMeta, abstractmethod

class State():
    __metaclass__=ABCMeta

    @abstractmethod
    def Next(self):
        """Получить следующее состояние"""