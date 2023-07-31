print('Enter your numbers. For quit enter \'q\'')
while True:
	number_1 = input('Input first number: ')
	if number_1 == 'q':
		break
	number_2 = input('Input second number: ')
	if number_2 == 'q':
		break
	try:
		result = int(number_1) + int(number_2)
	except ValueError:
		print('Your enter not number!')
	else:
		print(f'Sum of two numbers is: {str(result)}')
print('Finish')