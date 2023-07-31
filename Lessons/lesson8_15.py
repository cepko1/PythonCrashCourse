import makecar


car1 = makecar.make_car('subaru', 'outback', color='blue', tow_package=True)
print(car1)
car2 = makecar.make_car('WV', 'golf', color='black')
for key, value in car2.items():
	print(f'{key}: {value}')