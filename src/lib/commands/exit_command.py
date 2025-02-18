from src.lib.commands.base_command import BaseCommand


class ExitCommand(BaseCommand):
    def execute(self, args):
        """
        Ignores any arguments and terminates the program.
        """
        exit(0)

    def info(self):
        """
        Display information on how to use the exit command.
        """
        print("Command: exit")
        print("Description: Closes the application.")
        print("Usage: exit")
        print("Example: exit")
