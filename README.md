```md
# 🚀 Taskly – A CLI Task Manager

**Taskly** is a lightweight, modular CLI-based tool for quick task management. It uses SQLite as a database and follows a command-based architecture for flexibility and easy expansion.

---

## 📖 Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features
✅ Simple and fast CLI-based task management  
✅ Modular command system for easy extension  
✅ SQLite-powered persistent storage  
✅ Lightweight and dependency-free  

---

## 🛠 Installation
Clone the repository and navigate into the directory:

```sh
git clone https://github.com/8xMohab/taskly.git
cd taskly
```

Ensure you have Python 3 installed, then set up the environment:

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
pip install -r requirements.txt  # If dependencies exist
```

---

## 🚀 Usage
Run the program using:

```sh
python main.py
```

You'll be prompted to enter a command.

For example, to add a task:

```sh
$ add Buy groceries
```

To display all tasks:

```sh
$ tasks
```

To exit:

```sh
$ exit
```

---

## ⚡ Commands
| Command  | Description                          | Usage Example                     |
|----------|--------------------------------------|-----------------------------------|
| `add`    | Adds a new task                      | `add Buy groceries`               |
| `tasks`  | Displays the current task list       | `tasks`                           |
| `help`   | Shows help for all commands          | `help` or `help add`              |
| `exit`   | Exits the application                | `exit`                            |

---

## 🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📜 License
This project is open-source and available under the GNU General Public License.
```
