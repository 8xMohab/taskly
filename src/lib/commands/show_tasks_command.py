from src.lib.commands.base_command import BaseCommand
from src.lib.db_actions import get_tasks
from src.lib.utl import display_tasks, display_box


class ShowTasksCommand(BaseCommand):
    def execute(self, args):
        tasks = get_tasks()
        if tasks:
            display_tasks(tasks)
        else:
            display_box("  No tasks found. Add some!")

    def info(self):
        print("Command: tasks")
        print("Description: Displays all current tasks.")
        print("Usage: tasks")
        print("Example: tasks")
