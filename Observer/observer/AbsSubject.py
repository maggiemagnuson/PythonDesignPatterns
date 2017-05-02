import abc

from Observer.observer.AbsObserver import AbsObserver

class AbsSubject(metaclass=abc.ABCMeta):

    ###
    # Use a set to ensure there are no duplicate entries
    ###
    _observers = set()

    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError('Observer not derived from AbsObserver')
        self._observers.add(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, value=None):
        for observer in self._observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)

    ###
    # The following is needed to turn this class
    # into a Pyton Context Manager, which will
    # ensure there are no dangling references and
    # will allow garbage collection to happen
    ###
    def __enter__(self):
        return self

    ###
    # This will clean up observers and ensure we
    # don't have any dangling references which will
    # block garbage collection.
    ###
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._observers.clear()