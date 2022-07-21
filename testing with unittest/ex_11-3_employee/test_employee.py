# write a test case for Employee
# write two test methods test_give_default_raise() and test_give_custom_raise()
# use the setUp() method so you don't have to create a new employee instance in each test method
# run your test case and make sure both tests pass

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""

    def setUp(self):
        """Create employee instance to use in all test methods"""
        self.employee = Employee(first_name='John', last_name='Grey', annual_salary=70_000)

    def test_give_default_raise(self):
        """Test the default raise"""
        raised_salary = self.employee.give_raise()
        self.assertEqual(75_000, raised_salary)

    def test_give_custom_raise(self):
        """Test the custom raise"""
        raised_salary = self.employee.give_raise(1000)
        self.assertEqual(71_000, raised_salary)

if __name__ == '__main__':
    unittest.main()
