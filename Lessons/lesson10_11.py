import json

def read_number(file):
	""" Read number from JSON file"""
	
	try:
		with open(file) as f:
			number = json.load(f)
			return number
	except FileNotFoundError:
		return None
		
def write_number(file):
	with open(file, 'w') as f:
		number = input('Please enter your favoirite number: ')
		json.dump(number, f)

def show_number(num):
	print(f"Your favourite number is {num}")
	isyour = input('Is it your number (Y//N): ')
	if isyour.upper() == 'Y':
		print('Excelent')
	else:
		write_number(filename)
		
		
filename = "favourite.json"
num = read_number(filename)
if num:
	show_number(num)
else:
	write_number(filename)