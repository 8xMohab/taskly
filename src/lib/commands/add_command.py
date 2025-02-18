from src.lib.commands.base_command import BaseCommand
from src.lib.commands.show_tasks_command import ShowTasksCommand
from src.lib.db_actions import add_task


class AddCommand(BaseCommand):
    def execute(self, args):
        if args:
            success = add_task(args)
            if success:
                tasks = ShowTasksCommand()
                tasks.execute("")

            else:
                print("Error: Failed to add task.")
        else:
            print("Error: No task provided. Usage:")
            self.info()

    def info(self):
        """
        Display information on how to use the add command.
        """
        print("Command: add")
        print("Description: Adds a new task to the todo list.")
        print("Usage: add <task>")
        print("Example: add Walk the dog.")
