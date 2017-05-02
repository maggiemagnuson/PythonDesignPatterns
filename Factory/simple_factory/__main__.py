from Factory.simple_factory.autofactory import AutoFactory

factory = AutoFactory()

for carname in 'ChevyVolt', 'FordFocus', 'JeepSahara', 'Tesla P90D', 'DodgeDurango':
    car = factory.create_instance(carname)
    car.start()
    car.stop()