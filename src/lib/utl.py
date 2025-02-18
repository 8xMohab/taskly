def display_box(text):
    # Define the width of the box
    width = 50

    # Top border
    print("=" * width)

    # Empty line with borders
    print("||" + " " * (width - 4) + "||")

    # Text line: add a space before the text and pad the rest
    text_line = " " + text
    text_line = text_line.ljust(width - 4)
    print("||" + text_line + "||")

    # Another empty line with borders
    print("||" + " " * (width - 4) + "||")

    # Bottom border
    print("=" * width)


def display_tasks(tasks):
    tasks_str = ""
    if tasks:
        for task in tasks:
            tasks_str += f"  {task[0]}. {task[1]}\n"
    else:
        tasks_str = "  No tasks found. Add some!"

    display_box(tasks_str.strip())
