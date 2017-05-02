class Order(object):
    def __init__(self, weight=None):
        self._weight=weight

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value
