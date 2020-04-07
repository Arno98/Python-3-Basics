import unittest
from employee_module import Employee

class TestEmployee(unittest.TestCase):
	
	def setUp(self):
		self.employee = Employee("Ed", "Jackson", 100000)
		
	def test_give_standart_raise(self):
		self.assertEqual(self.employee.give_raise(), 105000)
		
	def test_give_costum_raise(self):
		self.assertEqual(self.employee.give_raise(money_plus=100000), 200000)
		
unittest.main()
