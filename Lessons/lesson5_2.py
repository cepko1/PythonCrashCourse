print('How old are you')
age = int(input ('Enter age:'))
if age < 2:
	print ('You are newborn')
elif age < 4:
	print('You are baby')
elif age < 13:
	print('You are child')
elif age < 20:
	print('You are teenager')
elif age < 65:
	print('You are adult')
else:
	print('You are old man')