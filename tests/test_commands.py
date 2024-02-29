import pytest
from app import App

def test_greet_command(capfd):
    app = App()
    app.load_commands()

    command_handler = app.command_handler
    greet_command = command_handler.commands.get("greet")
    assert greet_command is not None, "GreetCommand should be registered"

    # Test without args and kwargs
    greet_command.execute()
    out, err = capfd.readouterr()
    assert out == "Hello, World!\n", "The GreetCommand should print 'Hello, World!'"

    # Test with args and kwargs
    greet_command.execute("Alice", greeting="Hi")
    out, err = capfd.readouterr()
    assert out == "Hi, Alice!\n", "The GreetCommand should print 'Hi, Alice!'"

def test_goodbye_command(capfd):
    app = App()
    app.load_commands()

    command_handler = app.command_handler
    goodbye_command = command_handler.commands.get("goodbye")
    assert goodbye_command is not None, "GoodbyeCommand should be registered"

    # Test without args and kwargs
    goodbye_command.execute()
    out, err = capfd.readouterr()
    assert out == "Goodbye\n", "The GoodbyeCommand should print 'Goodbye'"

    # Test with args and kwargs
    goodbye_command.execute("See you", farewell="Adios")
    out, err = capfd.readouterr()
    assert out == "See you\n", "The GoodbyeCommand should print 'See you'"

def test_add_command(capfd):
    app = App()
    app.load_commands()

    command_handler = app.command_handler
    add_command = command_handler.commands.get("add")
    assert add_command is not None, "AddCommand should be registered"

    # Test with correct number of arguments
    add_command.execute(["2", "3"])
    out, err = capfd.readouterr()
    assert out == "Result: 5.0\n", "The AddCommand should print 'Result: 5.0'"

    # Test with incorrect number of arguments
    add_command.execute(["2"])
    out, err = capfd.readouterr()
    assert out == "Invalid number of arguments for 'add' command.\n", "The AddCommand should print 'Invalid number of arguments for 'add' command.'"

def test_multiply_command(capfd):
    app = App()
    app.load_commands()

    command_handler = app.command_handler
    multiply_command = command_handler.commands.get("multiply")
    assert multiply_command is not None, "MultiplyCommand should be registered"

    # Test with correct number of arguments
    multiply_command.execute(["2", "3"])
    out, err = capfd.readouterr()
    assert out == "Result: 6.0\n", "The MultiplyCommand should print 'Result: 6.0'"

     # Test with incorrect number of arguments
    multiply_command.execute(["2"])
    out, err = capfd.readouterr()
    assert out == "Invalid number of arguments for 'multiply' command.\n", "The MultiplyCommand should print 'Invalid number of arguments for 'multiply' command.'"

    multiply_command.execute(["2", "3", "4"])
    out, err = capfd.readouterr()
    assert out == "Invalid number of arguments for 'multiply' command.\n", "The MultiplyCommand should print 'Invalid number of arguments for 'multiply' command.'"

def test_divide_command(capfd):
    app = App()
    app.load_commands()

    command_handler = app.command_handler
    divide_command = command_handler.commands.get("divide")
    assert divide_command is not None, "DivideCommand should be registered"

    # Test with correct number of arguments
    divide_command.execute(["6", "2"])
    out, err = capfd.readouterr()
    assert out == "Result: 3.0\n", "The DivideCommand should print 'Result: 3.0'"

    # Test with division by zero
    divide_command.execute(["6", "0"])
    out, err = capfd.readouterr()
    assert out == "Error: Cannot divide by zero.\n", "The DivideCommand should print 'Error: Cannot divide by zero.'"

    # Test with incorrect number of arguments
    divide_command.execute(["6"])
    out, err = capfd.readouterr()
    assert out == "Invalid number of arguments for 'divide' command.\n", "The DivideCommand should print 'Invalid number of arguments for 'divide' command.'"

    divide_command.execute(["6", "2", "3"])
    out, err = capfd.readouterr()
    assert out == "Invalid number of arguments for 'divide' command.\n", "The DivideCommand should print 'Invalid number of arguments for 'divide' command.'"

def test_subtract_command(capfd):
    app = App()
    app.load_commands()

    command_handler = app.command_handler
    subtract_command = command_handler.commands.get("subtract")
    assert subtract_command is not None, "SubtractCommand should be registered"

    # Test with correct number of arguments
    subtract_command.execute(["5", "3"])
    out, err = capfd.readouterr()
    assert out == "Result: 2.0\n", "The SubtractCommand should print 'Result: 2.0'"

    # Test with incorrect number of arguments
    subtract_command.execute(["5"])
    out, err = capfd.readouterr()
    assert out == "Invalid number of arguments for 'subtract' command.\n", "The SubtractCommand should print 'Invalid number of arguments for 'subtract' command.'"

    subtract_command.execute(["5", "3", "2"])
    out, err = capfd.readouterr()
    assert out == "Invalid number of arguments for 'subtract' command.\n", "The SubtractCommand should print 'Invalid number of arguments for 'subtract' command.'"

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    app = App()
    app.load_commands()

    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit) as e:
        app.start()
    assert str(e.value) == "Exiting...\nExit Code: 0", "The app did not exit as expected"

def test_menu_command(capfd):
    app = App()
    app.load_commands()

    command_handler = app.command_handler
    menu_command = command_handler.commands.get("menu")
    assert menu_command is not None, "MenuCommand should be registered"

    # Execute MenuCommand
    menu_command.execute()
    out, err = capfd.readouterr()
    expected_output = """Available Commands:
- multiply
- goodbye
- divide
- exit
- greet
- subtract
- menu
- add
"""
    assert out == expected_output, "MenuCommand did not print the expected output"
