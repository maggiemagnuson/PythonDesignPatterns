from Command.command_executor_refactor.CreateOrder import CreateOrder
from Command.command_executor_refactor.UpdateOrder import UpdateOrder
from Command.command_executor_refactor.ShipOrder import ShipOrder
from Command.command_executor_refactor.NoCommand import NoCommand

import sys

def get_commands():
    #Add all the potential commands
    commands = (CreateOrder, UpdateOrder, ShipOrder)
    return dict([cls.name, cls] for cls in commands)

def print_usage(commands):
    print('Usage: python -m Command CommandName [arguments]')
    print('Commands:')
    for command in commands.values():
        print(f'    {command.description}')

def parse_commands(commands, args):
    #This looks up values in dictionary based on first commandline arg
    command = commands.setdefault(args[0], NoCommand)
    return command(args)

# Main()
# Create the dictionary of valid commands
commands = get_commands()
# Make sure we have a valid number of commandline args
if len(sys.argv) < 2:
    print_usage(commands)
    exit()
# Parse the command to get back right class
command = parse_commands(commands, sys.argv[1:])
# Execute based on class returned above
command.execute()
