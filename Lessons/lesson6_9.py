peoples = {
	'biden' : {
		'name' : 'john',
		'country' : 'USA',
		'numbers': [3, 5, 2]
	},
	'macron': {
		'name' : 'emanuel',
		'country': 'france',
		'numbers': [1, 2, 4, 5, 6]
	},
	'zelensky': {
		'name': 'volodymyr',
		'country': 'ukraine',
		'numbers': [3, 5, 7, 9]
	}
}

for people, data in peoples.items():
	print(f"Prezidend's {people.title()} name is {data['name'].title()}")
	print('His numbers is:', end= ' ')
	for number in data['numbers']:
		print(number, end = ', ')
	print()