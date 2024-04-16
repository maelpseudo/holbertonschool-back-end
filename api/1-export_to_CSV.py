import requests
import sys
import csv

def export_tasks_to_csv(employee_id):
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

    # CSV File Writing
    file_name = f'{employee_id}.csv'
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([employee_id, user_data['username'], task['completed'], task['title']])

    print(f"Data successfully written to {file_name}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    
    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    export_tasks_to_csv(emp_id)
