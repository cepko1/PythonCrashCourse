def make_car(brand, model, **kwargs):
		kwargs['brand'] = brand
		kwargs['model'] = model
		return kwargs
		
		
car1 = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car1)
car2 = make_car('WV', 'golf', color='black')
for key, value in car2.items():
	print(f'{key}: {value}')