import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
	"""Test Employee class"""
	
	def setUp(self):
		"""Setup typical object of employee"""
		self.name = 'Andy'
		self.surname ='Johnson'
		self.sallary = 50000
		self.tested_employee = Employee(self.name,self.surname,self.sallary)
	
	def test_give_default_raise(self):
		"""Testing raise sallary by default without argument"""
		self.tested_employee.give_raise()
		self.assertEqual(self.tested_employee.sallary,55000)
		
	def test_give_custom_raise(self):
		"""Testing custom sallary raise"""
		self.tested_employee.give_raise(11111)
		self.assertEqual(self.tested_employee.sallary,61111)
		
	def test_correct_employee_creation(self):
		"""Test arguments of object"""
		self.assertEqual(self.tested_employee.name, self.name)
		self.assertEqual(self.tested_employee.surname, self.surname)
		self.assertEqual(self.tested_employee.sallary, self.sallary)
	
if __name__ == '__main__':
	unittest.main()