import sys
from app.commands import Command


class ExitCommand(Command):
    def execute(self, *args, **kwargs):
        exit_message = "Exiting..." if args else "Exiting..."
        exit_code = kwargs.get('exit_code', 0)
        sys.exit(f"{exit_message}\nExit Code: {exit_code}")