from inspect import getmembers, isclass, isabstract

import Factory.simple_factory.autos

class AutoFactory(object):
    autos = {}

    def __init__(self):
        self.load_autos()

    def load_autos(self):
        classes = getmembers(Factory.simple_factory.autos,
                             lambda m: isclass(m) and not isabstract(m))
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, Factory.simple_factory.autos.AbsAuto):
                self.autos.update([[name, _type]])

    def create_instance(self, carname):
        if carname in self.autos:
            return self.autos[carname]()
        else:
            return Factory.simple_factory.autos.NullCar(carname)