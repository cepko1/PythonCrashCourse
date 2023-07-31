class Employee:
	def __init__(self,name, surname, sallary):
		self.name = name
		self.surname = surname
		self.sallary = sallary
		
	def give_raise(self, amount = 5000):
		self.sallary += amount