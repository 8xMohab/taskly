#!/usr/bin/env python3

from src.lib.db_actions import init_db
from src.lib.commands.show_tasks_command import ShowTasksCommand
from src.lib.commands.command_factory import get_command
from src.lib.commands.help_command import HelpCommand


def main():
    # Application startup
    init_db()  # Create a database if it doesn't exist
    tasks = ShowTasksCommand()
    tasks.execute("")
    print()

    while True:
        # Parse the input into command and (optional) arguments
        user_input = input("$ ").strip()
        parts = user_input.split(" ", 1)
        command_name = parts[0].strip()
        args = parts[1].strip() if len(parts) > 1 else ""

        # Handle help command explicitly
        if command_name == "help":
            help_command = HelpCommand()
            help_command.execute(args)
        elif command_name == "":
            continue
        else:
            # Retrieve and execute other commands
            command = get_command(command_name)
            if command:
                command.execute(args)
            else:
                print(f"Command '{command_name}' not recognized.")


if __name__ == "__main__":
    main()
