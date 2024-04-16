import requests
import json

def export_all_tasks():
    # API endpoints
    base_url = 'https://jsonplaceholder.typicode.com'
    users_url = f'{base_url}/users'
    todos_url = f'{base_url}/todos'

    # Fetching all user data
    users_response = requests.get(users_url)
    if users_response.status_code != 200:
        print('Error fetching users')
        return
    users_data = users_response.json()

    # Fetching all todos data
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print('Error fetching todos')
        return
    todos_data = todos_response.json()

    # Organize tasks by user
    task_dict = {}
    for user in users_data:
        user_tasks = [task for task in todos_data if task['userId'] == user['id']]
        task_list = [
            {"username": user['username'], "task": task['title'], "completed": task['completed']}
            for task in user_tasks
        ]
        task_dict[user['id']] = task_list

    # JSON File Writing
    file_name = 'todo_all_employees.json'
    with open(file_name, 'w') as json_file:
        json.dump(task_dict, json_file, indent=4)

    print(f"Data successfully written to {file_name}")

if __name__ == '__main__':
    export_all_tasks()
