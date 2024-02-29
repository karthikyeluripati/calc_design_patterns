import pytest
from app import App
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand
from app.commands.exit import ExitCommand
from app.commands.menu import MenuCommand
from app.commands import CommandHandler

def test_greet_command(capfd):
    command = GreetCommand()

    # Test without args and kwargs
    command.execute()
    out, err = capfd.readouterr()
    assert out == "Hello, World!\n", "The GreetCommand should print 'Hello, World!'"

    # Test with args and kwargs
    command.execute("Alice", greeting="Hi")
    out, err = capfd.readouterr()
    assert out == "Hi, Alice!\n", "The GreetCommand should print 'Hi, Alice!'"

def test_goodbye_command(capfd):
    command = GoodbyeCommand()

    # Test without args and kwargs
    command.execute()
    out, err = capfd.readouterr()
    assert out == "Goodbye\n", "The GoodbyeCommand should print 'Goodbye'"

    # Test with args and kwargs
    command.execute("See you", farewell="Adios")
    out, err = capfd.readouterr()
    assert out == "See you\n", "The GoodbyeCommand should print 'See you'"

def test_add_command(capfd):
    command = AddCommand()

    # Test with correct number of arguments
    command.execute(["2", "3"])
    out, err = capfd.readouterr()
    assert out == "Result: 5.0\n", "The AddCommand should print 'Result: 5.0'"

    # Test with incorrect number of arguments
    command.execute(["2"])
    out, err = capfd.readouterr()
    assert out == "Invalid number of arguments for 'add' command.\n", "The AddCommand should print 'Invalid number of arguments for 'add' command.'"

def test_divide_command(capfd):
    command = DivideCommand()

    # Test with correct number of arguments
    command.execute(["6", "2"])
    out, err = capfd.readouterr()
    assert out == "Result: 3.0\n", "The DivideCommand should print 'Result: 3.0'"

    # Test with division by zero
    command.execute(["6", "0"])
    out, err = capfd.readouterr()
    assert out == "Error: Cannot divide by zero.\n", "The DivideCommand should print 'Error: Cannot divide by zero.'"

     # Test with incorrect number of arguments
    command.execute(["6"])
    out, err = capfd.readouterr()
    assert out == "Invalid number of arguments for 'divide' command.\n", "The DivideCommand should print 'Invalid number of arguments for 'divide' command.'"

    command.execute(["6", "2", "3"])
    out, err = capfd.readouterr()
    assert out == "Invalid number of arguments for 'divide' command.\n", "The DivideCommand should print 'Invalid number of arguments for 'divide' command.'"

def test_multiply_command(capfd):
    command = MultiplyCommand()

    # Test with correct number of arguments
    command.execute(["2", "3"])
    out, err = capfd.readouterr()
    assert out == "Result: 6.0\n", "The MultiplyCommand should print 'Result: 6.0'"

     # Test with incorrect number of arguments
    command.execute(["2"])
    out, err = capfd.readouterr()
    assert out == "Invalid number of arguments for 'multiply' command.\n", "The MultiplyCommand should print 'Invalid number of arguments for 'multiply' command.'"

    command.execute(["2", "3", "4"])
    out, err = capfd.readouterr()
    assert out == "Invalid number of arguments for 'multiply' command.\n", "The MultiplyCommand should print 'Invalid number of arguments for 'multiply' command.'"

def test_subtract_command(capfd):
    command = SubtractCommand()

    # Test with correct number of arguments
    command.execute(["5", "3"])
    out, err = capfd.readouterr()
    assert out == "Result: 2.0\n", "The SubtractCommand should print 'Result: 2.0'"

    # Test with incorrect number of arguments
    command.execute(["5"])
    out, err = capfd.readouterr()
    assert out == "Invalid number of arguments for 'subtract' command.\n", "The SubtractCommand should print 'Invalid number of arguments for 'subtract' command.'"

    command.execute(["5", "3", "2"])
    out, err = capfd.readouterr()
    assert out == "Invalid number of arguments for 'subtract' command.\n", "The SubtractCommand should print 'Invalid number of arguments for 'subtract' command.'"

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert str(e.value) == "Exiting...\nExit Code: 0", "The app did not exit as expected"

def test_menu_command(capfd):
    command_handler = CommandHandler()
    menu_command = MenuCommand(command_handler)

    # Register commands
    command_handler.register_command("greet", GreetCommand())
    command_handler.register_command("goodbye", GoodbyeCommand())
    command_handler.register_command("exit", ExitCommand())
    command_handler.register_command("add", AddCommand())
    command_handler.register_command("subtract", SubtractCommand())
    command_handler.register_command("multiply", MultiplyCommand())
    command_handler.register_command("divide", DivideCommand())
    command_handler.register_command("menu", menu_command)

    # Execute MenuCommand
    menu_command.execute()
    out, err = capfd.readouterr()
    expected_output = """Available Commands:
- greet
- goodbye
- exit
- add
- subtract
- multiply
- divide
- menu
"""
    assert out == expected_output, "MenuCommand did not print the expected output"
