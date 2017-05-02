from Factory.simple_factory.autos.abs_auto import AbsAuto

class NullCar(AbsAuto):
    def __init__(self, carname):
        self._carname = carname

    def start(self):
        print(f"{self._carname} ain't no car I'd ever heard of")

    def stop(self):
        pass