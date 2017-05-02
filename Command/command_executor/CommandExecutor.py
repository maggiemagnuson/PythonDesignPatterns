
class CommandExecutor(object):

    def execute_command(self, args):
        if args[0] == 'CreateOrder':
            self.create_order()
        elif args[0] == 'UpdateQuantity':
            self.update_quantity(args[1])
        elif args[0] == 'ShipOrder':
            self.ship_order()
        else:
            print (f'Unrecognized command: {args[0]}')

    def create_order(self):
        pass

    def update_quantity(self, quantity):
        print (quantity)
        old_quantity = 5
        print ('Database Updated')
        print (f'Logging updated quantity from {old_quantity} to {quantity}')

    def ship_order(self):
        pass