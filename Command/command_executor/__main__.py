import sys
from Command.command_executor.CommandExecutor import  CommandExecutor


if len(sys.argv) < 2:
    print('Usage: <command>')
    print('Commands:')
    print('    CreateOrder')
    print('    UpdateQuantity <number>')
    print('    ShipOrder')
    exit()

executor = CommandExecutor()
executor.execute_command(sys.argv[1:])