import os
import sqlite3


# Build the database file path based on the current working directory
DB_FILE = os.path.join(os.getcwd(), "data", "todo.db")


def init_db():
    """
    Initialize the database if it doesn't exist.
    """

    # Ensure the directory for the database exists
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)

    if not os.path.exists(DB_FILE):
        print("Database not found. Initializing...")
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                done BOOLEAN DEFAULT 0
            )
            """
        )
        conn.commit()
        conn.close()

    print("\n  Taskly")


def get_tasks():
    """
    Fetch all tasks from the database.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT id, task FROM tasks")
    tasks = cursor.fetchall()  # Fetch all rows from the tasks table
    conn.close()

    return tasks


def add_task(task: str) -> bool:

    if not task or not task.strip():
        return False

    safe_task = (
        task.strip()
        # The parameterized query will protect against SQL injection.
    )

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (safe_task,))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print("Error adding task:", e)
        return False
