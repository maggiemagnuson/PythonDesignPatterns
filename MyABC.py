import abc

class MyABC(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def do_something(self, value):
        """ Required method """

    @property
    @abc.abstractmethod
    def some_property(self):
        """ Required property """