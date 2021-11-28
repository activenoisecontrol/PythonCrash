import unittest
from employee import Employee

class EmployeeTest(unittest.TestCase):
    """Test for the class Employee"""

    def setUp(self):
        self.emp1 = Employee('alek', 'bolduin', 5000)

    def test_default_salary_raise(self):
        self.emp1.give_raise()
        self.assertEqual(self.emp1.salary, 10000)

    def test_custom_salary_raise(self):
        self.emp1.give_raise(15000)
        self.assertEqual(self.emp1.salary, 20000)

if __name__ == '__main__':
    unittest.main()