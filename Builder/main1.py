#from Builder.computer import Computer
from Builder.impl3_computer import ComputerImpl3
from Builder.director import Director

if __name__ == '__main__':

#    computer = Computer()
#    computer.case="Coolermaster N300"
#    computer.mainboard="MSI 970"
#    computer.cpu="Intel Core i7-4770"
#    computer.memory="Corsair Vengeance 16GB"
#    computer.hard_drive="Segate 2TB"
#    computer.video_card="GeForce GTX 1070"
#    computer.display()

    builder = ComputerImpl3()
    director = Director(builder)
    director.build_computer()
    computer = director.get_computer()
    computer.display()