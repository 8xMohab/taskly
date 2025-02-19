from src.lib.commands.base_command import BaseCommand
from src.lib.db_actions import remove_task
from src.lib.commands.show_tasks_command import ShowTasksCommand


class RemoveTaskCommand(BaseCommand):
    def execute(self, args):
        # Check if an argument (task ID) was provided
        if not args.strip():
            print("Error: No task ID provided.")
            self.info()
            return

        # Validate that the provided argument is a number
        try:
            task_id = int(args.strip())
        except ValueError:
            print("Error: Task ID must be a valid number.")
            return

        # Call the db action to remove the task and get the result
        result = remove_task(task_id)
        success, message = result[0], result[1]

        if success:
            tasks = ShowTasksCommand()
            tasks.execute("")

        else:
            print(f"Error: {message}")

    def info(self):
        print("Command: remove")
        print("Description: Removes a task by its ID from the task list.")
        print("Usage: remove <task_id>")
        print("Example: remove 1")
