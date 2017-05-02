import abc

class AbsObserver(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def update(cls):
        """Required"""

    ###
    # The following is needed to turn this class
    # into a Pyton Context Manager, which will
    # ensure there are no dangling references and
    # will allow garbage collection to happen
    ###
    def __enter__(self):
        return self

    ###
    # This is abstract so it will need to be implemented
    # by the concrete class.
    ##
    @abc.abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass