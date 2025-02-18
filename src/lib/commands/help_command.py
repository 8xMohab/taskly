from src.lib.commands.base_command import BaseCommand
from src.lib.commands.command_factory import get_command, get_all_commands


class HelpCommand(BaseCommand):
    def execute(self, args=""):
        if args:
            if args == "help":
                self.info()
                print()
            else:
                command = get_command(args)
                if command:
                    command.info()
                    print()
                else:
                    print(f"Command '{args}' not recognized.\n")
        else:

            commands = get_all_commands()
            for name, command in commands.items():
                print("-" * 50)
                command.info()
                print()  # extra newline for spacing

            print("-" * 50)
            self.info()
            print()  # extra newline for spacing

    def info(self):
        print("Command: help")
        print(
            "Description: Displays this message. Use 'help <command>' to get info on a specific command."
        )
        print("Usage: help <command>")
        print("Example: help add")
