class Restaurant:
	""" Simple restaurant model"""
	
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		nymber_served =0
		
	def describe_restaurant(self):
		print(f'The restaurant is \'{self.restaurant_name}\'. \nThe restaurant\'s cuisine is {self.cuisine_type}')
		
	def set_number_served(self, number):
		if number > 0:
			self.number_served = number
			
	def increment_number_served(self, number):
		self.number_served += number
		
		
monaco = Restaurant('Monaco', 'italian')
monaco.describe_restaurant()
monaco.set_number_served(12)
print(f'In the restaurant{monaco.restaurant_name} served {monaco.number_served} places')
monaco.increment_number_served(5)
print(f'In the restaurant{monaco.restaurant_name} served {monaco.number_served} places')