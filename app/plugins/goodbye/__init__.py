from app.commands import Command

class GoodbyeCommand(Command):
    def execute(self, *args, **kwargs):
        farewell_message = args[0] if args else "Goodbye"
        print(f"{farewell_message}")