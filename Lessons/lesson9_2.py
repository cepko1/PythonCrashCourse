class Restaurant:
	""" Simple restaurant model"""
	
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		print(f'The restaurant is \'{self.restaurant_name}\'. \nThe restaurant\'s cuisine is {self.cuisine_type}')
		
		
monaco = Restaurant('Monaco', 'italian')
monaco.describe_restaurant()