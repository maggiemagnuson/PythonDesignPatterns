from Factory.simple_factory.autos.abs_auto import AbsAuto

class FordFocus(AbsAuto):

    def start(self):
        print("Ford Focus is running smoothly")

    def stop(self):
        print("Ford Focus shutting down")