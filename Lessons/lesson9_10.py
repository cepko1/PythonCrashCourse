from restaurant import Restaurant
from icecream import IceCreamStand

		
monaco = Restaurant('Monaco', 'italian')
monaco.describe_restaurant()
monaco.set_number_served(12)
print(f'In the restaurant{monaco.restaurant_name} served {monaco.number_served} places')
monaco.increment_number_served(5)
print(f'In the restaurant{monaco.restaurant_name} served {monaco.number_served} places')
icecream = IceCreamStand('IceWorld', 'Deserts')
icecream.describe_restaurant()
icecream.set_flavors(['Cherry', 'Chocolate', 'Banana', 'Lime'])
icecream.show_flavors()