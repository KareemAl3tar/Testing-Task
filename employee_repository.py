import requests

class EmployeeRepository:
    def get_employees(self):
        response = requests.get("https://api.example.com/employees")
        if response.status_code == 200:
            employees = response.json()
            return sorted(employees, key=lambda x: x['id'])
        else:
            return []
