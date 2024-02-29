from app.commands import Command

class DivideCommand(Command):
    def execute(self, args):
        if len(args) == 2:
            try:
                result = float(args[0]) / float(args[1])
                print(f"Result: {result}")
            except ZeroDivisionError:
                print("Error: Cannot divide by zero.")
        else:
            print("Invalid number of arguments for 'divide' command.")