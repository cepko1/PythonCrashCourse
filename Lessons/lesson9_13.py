from random import randint

class Die:
	""" Simple represent of die"""
	
	def __init__(self, sides = 6):
		self.sides = sides
		
	def roll_die(self):
		x = randint(1, self.sides)
		return x
		
die1= Die()
for i in range(5):
	print(die1.roll_die())
print()
die2 = Die(10)
for i in range(10):
 	print(die2.roll_die())