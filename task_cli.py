import argparse
import json
import sys

from datetime import datetime

def load_task():
    try:
        # read json file
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"tasks": []}


def save_task(data):
    # write json file
    with open('tasks.json', 'w') as file:
        json.dump(data, file, indent=4, default=str)


def add_task(description):
    tasks = load_task()

    if tasks["tasks"]:
        new_task_id = max(task["task_id"] for task in tasks["tasks"]) + 1
    else:
        new_task_id = 1

    new_task = {
        "task_id": new_task_id,
        "task_description": description,
        "status": "todo",
        "createDate": datetime.now(),
        "updateDate": datetime.now()
    }
    tasks["tasks"].append(new_task)
    save_task(tasks)
    print(f'Task {new_task["task_id"]} added success!')


def update_tasks(task_id, new_description):
    tasks = load_task()
    for task in tasks["tasks"]:
        if task['task_id'] == task_id:
            task['task_description'] = new_description
            task['updateDate'] = datetime.now()
            save_task(tasks)
            print(f'Task {task["task_id"]} updated ({new_description}) success')
            return
    print(f'Task {task["task_id"]} is not found.')

def delete_task(task_id):
    tasks = load_task()
    task_found = False
    for task in tasks["tasks"]:
        if task['task_id'] == task_id:
            tasks["tasks"].remove(task)
            task_found = True
            save_task(tasks)
            print(f'Task {task_id} deleted successfully.')
            break
    if not task_found:
       print(f'Task {task_id} is not found')

def status_in_progress(task_id):
    tasks =load_task()
    for task in tasks["tasks"]:
        if task["task_id"] == task_id:
            task["status"] = "in-progress"
            task["updateDate"] = datetime.now()
            save_task(tasks)
            print(f'Task {task_id} status: in-progress')
            return

def status_done(task_id):
    tasks =load_task()
    for task in tasks["tasks"]:
        if task["task_id"] == task_id:
            task["status"] = "done"
            task["updateDate"] = datetime.now()
            save_task(tasks)
            print(f'Task {task_id} status: done')
            return

def list_tasks(status=None):
    tasks = load_task()
    for task in tasks["tasks"]:
        if status is None or task["status"] == status:
            print(f'ID: {task["task_id"]}, Description: {task["task_description"]}, Status: {task["status"]}, Created At: {task["createDate"]}, Updated At: {task["updateDate"]}')


def main():
    parser = argparse.ArgumentParser(description="TASK CLI")
    subparsers = parser.add_subparsers(dest="command")
 
    # for add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task Description")
    
    # for update command
    update_parser = subparsers.add_parser("update", help="Update task")
    update_parser.add_argument("id", type=int, help="Task ID")
    update_parser.add_argument("new_description", help="New Task Description")

    # for delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")
    
    # for status changes in-progress
    in_progress_parser = subparsers.add_parser("mark-in-progress", help="Task status change in-progress")
    in_progress_parser.add_argument("id", type=int, help="Task ID")
    
    # for status changes done
    done_parser = subparsers.add_parser("mark-done", help="Task status change done")
    done_parser.add_argument("id", type=int, help="Task ID")

    # for list command
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("status", nargs="?", choices=["todo", "in-progress", "done"])


    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    
    elif args.command == "update":
        update_tasks(args.id, args.new_description)

    elif args.command == "delete":
        delete_task(args.id)

    elif args.command == "list":
        list_tasks(args.status)

    elif args.command == "mark-in-progress":
        status_in_progress(args.id)
    
    elif args.command == "mark-done":
        status_done(args.id)

if __name__ == '__main__':
    main()



    

