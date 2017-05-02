import abc

class AbsOrderCommand(metaclass=abc.ABCMeta):

    @property
    @abc.abstractmethod
    def name(self):
        pass

    @property
    @abc.abstractmethod
    def description(self):
        pass