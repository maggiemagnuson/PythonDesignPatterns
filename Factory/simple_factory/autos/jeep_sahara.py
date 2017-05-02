from Factory.simple_factory.autos.abs_auto import AbsAuto

class JeepSahara(AbsAuto):

    def start(self):
        print("Jeep Sahara is running ruggedly")

    def stop(self):
        print("Jeep Sahara shutting down")