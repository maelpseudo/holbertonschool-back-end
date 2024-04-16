import requests
import sys
import json

def export_tasks_to_json(employee_id):
    # API endpoints
    base_url = 'https://jsonplaceholder.typicode.com'
    users_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    # Fetching user data
    user_response = requests.get(users_url)
    if user_response.status_code != 200:
        print(f'Error fetching data for user with ID {employee_id}')
        return
    user_data = user_response.json()

    # Fetching todos data
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f'Error fetching TODOs for user with ID {employee_id}')
        return
    todos_data = todos_response.json()

    # Format tasks into the specified JSON structure
    tasks_list = []
    for task in todos_data:
        tasks_list.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": user_data['username']
        })
    
    # Prepare to write to JSON
    user_tasks = {str(employee_id): tasks_list}

    # JSON File Writing
    file_name = f'{employee_id}.json'
    with open(file_name, 'w') as json_file:
        json.dump(user_tasks, json_file, indent=4)

    print(f"Data successfully written to {file_name}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)
    
    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    export_tasks_to_json(emp_id)
