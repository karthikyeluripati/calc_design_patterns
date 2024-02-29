from app.commands import CommandHandler
from app.commands.exit import ExitCommand
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.register_commands()

    def register_commands(self):
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())

    def start(self):
        print("Type 'exit' to exit.")
        while True:
            user_input = input(">>> ").strip().split()
            command_name = user_input[0]
            args = user_input[1:]
            self.command_handler.execute_command(command_name, args)