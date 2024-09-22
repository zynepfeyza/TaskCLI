# Task Management CLI

A simple command-line interface (CLI) project from [roadmap.sh](https://roadmap.sh/projects/task-tracker) for managing tasks, with the tasks stored in a JSON file for persistence. You can add, update, delete, and list tasks, as well as change their status.

## Features

- **Add Task**: Create a new task with a description.
- **Update Task**: Modify the description of an existing task.
- **Delete Task**: Remove a task from the list.
- **Change Task Status**: Mark tasks as "in-progress" or "done".
- **List Tasks**: Display all tasks or filter by status (todo, in-progress, done).

## Installation

1. Clone the repository or download the source code.
2. Ensure you have Python 3 installed on your system.
3. Navigate to the project directory.

## Usage

You can run the CLI with various commands:

## Add a New Task

```bash
# Adding a new task
python task_cli.py add "Your task description here"

# Updating tasks
python task_manager.py update <task_id> "New task description"

# Deleting tasks
python task_manager.py delete <task_id>

# Marking a task as in progress or done
python task_manager.py mark-in-progress <task_id>
python task_manager.py mark-done <task_id>

# Lİsting all tasks
python task_manager.py list

# Listing tasks by status
python task_manager.py list done
python task_manager.py list in-progress
python task_manager.py list todo
```

## Task Properties

Each task should have the following properties:

- **id**: A unique identifier for the task
- **description**: A short description of the task
- **status**: The status of the task (todo, in-progress, done)
- **createdAt**: The date and time when the task was created
- **updatedAt**: The date and time when the task was last updated