from Factory.brute_force.chevy_volt import ChevyVolt
from Factory.brute_force.ford_focus import FordFocus
from Factory.brute_force.jeep_sahara import JeepSahara
from Factory.brute_force.null_car import NullCar

def get_car(carname):
    if carname == "Chevy":
        return ChevyVolt()
    elif carname == "Ford":
        return FordFocus()
    elif carname == "Jeep":
        return JeepSahara()
    else:
        return NullCar()

for carname in 'Chevy', "Ford", "Jeep", "Tesla":
    car = get_car(carname)
    car.start()
    car.stop()