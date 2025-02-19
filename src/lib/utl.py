width = 64  # this is not dynamic fix it later


# used to display tasks list
def display_tasks(tasks=[]):
    # set the width equal to longest item in list
    # or to the minimum width
    task_length_offset = 4 + 4 + 2 + 4

    print("=" * width)
    print(f"||{' ' * (width - 4)}||")

    for index, task in enumerate(tasks, start=1):
        whiteSpace = width - (
            len(f"{task[0]}") + len(f"{task[1]}") +
            len(f"{index}") + task_length_offset
        )
        print(
            f"||  {index}. {task[1]} id: {task[0]}{
                ' ' * whiteSpace} ||"
        )

    print(f"||{' ' * (width - 4)}||")
    print("=" * width)


# used to display a list of simple strings
def display_box(text=[]):
    # set the width equal to longest item in list
    # or to the minimum width

    print("=" * width)
    print(f"||{' ' * (width - 4)}||")

    for item in text:
        # There's a bug with the tabs offset that
        # has been added at the end before the pipes
        display_box_offset = 4 + 4
        print(
            f"||  {item}{
                ' ' * (width - (len(item) + display_box_offset))}  ||"
        )

    print(f"||{' ' * (width - 4)}||")
    print("=" * width)
