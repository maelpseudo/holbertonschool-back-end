#!/usr/bin/python3
'''
Python script for exporting data in JSON format
'''
import json
import requests

if __name__ == "__main__":
    users_endpoint = 'https://jsonplaceholder.typicode.com/users'
    todos_endpoint = 'https://jsonplaceholder.typicode.com/todos'

    users_data = requests.get(users_endpoint).json()
    todos_data = requests.get(todos_endpoint).json()

    all_user_tasks = {}

    for user in users_data:
        user_id = str(user["id"])
        all_user_tasks[user_id] = []

        for task in todos_data:
            if task["userId"] == user["id"]:
                task_info = {
                    "username": user["username"],
                    "task": task["title"],
                    "completed": task["completed"]
                }
                all_user_tasks[user_id].append(task_info)

    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(all_user_tasks, json_file)
