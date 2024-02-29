from app.commands import Command

class SubtractCommand(Command):
    def execute(self, args):
        if len(args) == 2:
            result = float(args[0]) - float(args[1])
            print(f"Result: {result}")
        else:
            print("Invalid number of arguments for 'subtract' command.")