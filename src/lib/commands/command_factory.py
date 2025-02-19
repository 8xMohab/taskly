from src.lib.commands.add_command import AddCommand
from src.lib.commands.exit_command import ExitCommand
from src.lib.commands.show_tasks_command import ShowTasksCommand
from src.lib.commands.remove_task_command import RemoveTaskCommand


def get_all_commands():
    return {
        "add": AddCommand(),
        "remove": RemoveTaskCommand(),
        "tasks": ShowTasksCommand(),
        "exit": ExitCommand(),
    }


def get_command(command_name):
    return get_all_commands().get(command_name, None)
