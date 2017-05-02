from Command.command_executor_refactor.AbsCommand import AbsCommand
from Command.command_executor_refactor.AbsOrderCommand import AbsOrderCommand

class NoCommand(AbsCommand):
    def __init__(self, args):
        self._command=args[0]
        pass

    def execute(self):
        print(f'No command named {self._command}')