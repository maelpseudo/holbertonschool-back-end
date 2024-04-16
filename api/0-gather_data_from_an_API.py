import requests
import sys

def fetch_todo_list_progress(employee_id):
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

    # Extract required information
    employee_name = user_data['name']
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task['completed']]
    number_of_done_tasks = len(completed_tasks)

    # Output the data in the specified format
    print(f'Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):')
    for task in completed_tasks:
        print(f'\t {task["title"]}')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    fetch_todo_list_progress(emp_id)
