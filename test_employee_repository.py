import unittest
from unittest.mock import patch, MagicMock
from employee_repository import EmployeeRepository 

class TestEmployeeRepository(unittest.TestCase):

    @patch('employee_repository.requests.get')
    def test_get_employees_success(self, mock_get):
        # api البيانات الوهمية
        mock_data = [
            {"id": 3, "name": "Alice", "position": "Developer"},
            {"id": 1, "name": "Bob", "position": "Manager"},
            {"id": 2, "name": "Charlie", "position": "Designer"}
        ]

        # إعداد  mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        repo = EmployeeRepository()
        employees = repo.get_employees()

        self.assertEqual(len(employees), 3)
        self.assertTrue(all('id' in emp for emp in employees))

    @patch('employee_repository.requests.get')
    def test_get_employees_sorted_by_id(self, mock_get):
        mock_data = [
            {"id": 3, "name": "Alice", "position": "Developer"},
            {"id": 1, "name": "Bob", "position": "Manager"},
            {"id": 2, "name": "Charlie", "position": "Designer"}
        ]
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response

        repo = EmployeeRepository()
        employees = repo.get_employees()

        sorted_ids = [emp['id'] for emp in employees]
        self.assertEqual(sorted_ids, [1, 2, 3])

    @patch('employee_repository.requests.get')
    def test_get_employees_error_response(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        repo = EmployeeRepository()
        employees = repo.get_employees()

        self.assertEqual(employees, [])

if __name__ == '__main__':
    unittest.main()
