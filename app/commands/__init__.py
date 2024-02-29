from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str, *args, **kwargs):
        try:
            # Passing additional arguments to the command's execute method
            self.commands[command_name].execute(*args, **kwargs)
        except KeyError:
            print(f"No such command: {command_name}")