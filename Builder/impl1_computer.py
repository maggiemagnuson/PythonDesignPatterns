from Builder.computer import Computer

class ComputerImpl1(object):

    def get_computer(self):
        return self._computer

    def build_computer(self):
        computer = self._computer = Computer()
        computer.case = "Coolermaster N300"
        computer.mainboard = "MSI 970"
        computer.cpu = "Intel Core i7-4770"
        computer.memory = "Corsair Vengeance"
        computer.hard_drive="Seagate 2TB"
        computer.video_card = "GeForce GTX 1070"