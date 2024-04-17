#!/usr/bin/python3
""" export data in JSON format"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    # Fetch user data and tasks from the JSONPlaceholder API
    user_data = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".
        format(argv[1])).json()
    todo_data = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".
        format(argv[1])).json()

    # Extract relevant information from user data
    username = user_data.get("username")
    user_id = argv[1]

    # Prepare tasks data for export
    tasks = []
    for task in todo_data:
        task_dict = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        }
        tasks.append(task_dict)

    # Create a dictionary with user_id as the key and tasks as the value
    todos = {user_id: tasks}

    # Export tasks data to a JSON file named with the user_id
    with open("{}.json".format(user_id), 'w') as jsonfile:
        json.dump(todos, jsonfile)
