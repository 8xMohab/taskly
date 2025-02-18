class BaseCommand:
    def execute(self, args):
        """
        Execute the command with the given arguments.
        Must be implemented by subclasses.
        """
        raise NotImplementedError("You must implement the execute method.")

    def info(self):
        """
        Print information about what the command does and how to use it.
        Must be implemented by subclasses.
        """
        raise NotImplementedError("You must implement the info method.")
