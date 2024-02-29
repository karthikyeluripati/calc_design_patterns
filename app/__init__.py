import os
import imp
from app.commands import CommandHandler
from app.plugins.menu import MenuCommand

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.load_commands()

    def load_commands(self):
        command_directory = "app/plugins"  # Specify the directory where your command plugins are stored

        # Iterate through subdirectories in the command directory
        for subdirectory in os.listdir(command_directory):
            subdirectory_path = os.path.join(command_directory, subdirectory)
            
            if os.path.isdir(subdirectory_path):
                #try:
                    if subdirectory.lower() == "menu":
                        # If the subdirectory is "menu", instantiate MenuCommand with command_handler
                        command_instance = MenuCommand(self.command_handler)
                    else:
                        # Assuming the command file is named as command_name_command.py
                        command_file = f"__init__"
                        module = imp.load_source(command_file, os.path.join(subdirectory_path, f"__init__.py"))

                        # Assuming the command class is named as CommandNameCommand
                        command_class = getattr(module, f"{subdirectory.capitalize()}Command")
                        command_instance = command_class()

                    self.command_handler.register_command(subdirectory, command_instance)
                #except Exception as e:print(f"Error loading command from {subdirectory_path}: {str(e)}")

    def start(self):
        print("Type 'exit' to exit.")
        while True:
            user_input = input(">>> ").strip().split()
            
            if not user_input:
                print("Please enter a command.")
                continue
            
            command_name = user_input[0].lower()
            args = user_input[1:]

            #try:
            self.command_handler.execute_command(command_name, args)
            #except Exception as e:
            #    print(f"Error: {str(e)}")
