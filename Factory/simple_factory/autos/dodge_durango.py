from Factory.simple_factory.autos.abs_auto import AbsAuto

class DodgeDurango(AbsAuto):

    def start(self):
        print("Dodge Durango is running like a gas pig")

    def stop(self):
        print("Dodge Durango shutting down")