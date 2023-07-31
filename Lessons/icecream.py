from restaurant import Restaurant
class IceCreamStand(Restaurant):
#		def __init__(self, restaurant_name, cuisine_type)
#		super().__init__(restaurant_name, cuisine_type)

		def set_flavors(self, flavors):
			self.flavors = flavors
		def show_flavors(self):
			print(f'The flavors of {self.restaurant_name} are', end = ' ')
			for flavor in self.flavors:
				print(flavor, end = ' ')