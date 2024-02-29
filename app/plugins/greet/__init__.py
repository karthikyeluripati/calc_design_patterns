from app.commands import Command


class GreetCommand(Command):
    def execute(self, *args, **kwargs):
        name = args[0] if args else "World"
        greeting = kwargs.get('greeting', 'Hello')
        print(f"{greeting}, {name}!")