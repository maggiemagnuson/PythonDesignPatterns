from Command.command_executor_refactor.AbsCommand import AbsCommand

class UpdateOrder(AbsCommand):
    name = 'UpdateQuantity'
    description = 'UpdateQuantity <number>'

    def __init__(self, args):
        self.quantity = args[1]

    def execute(self):
        old_quantity=5
        #Simulate Database Update
        print('Updated database ...')
        #Simulate Logging the Update
        print(f'Logging: Updated quantity from {old_quantity} to {self.quantity}')