prompt = ('Please enter you age.')
prompt += ('\nIf you want stop please enter "stop" Enter your age: ')
age =''
flag = True
while flag:
	age = input(prompt)
	if age == 'stop':
		break
	age = int(age)
	if age < 3:
		cost = 'free'
	elif 3 <= age <= 12:
		cost = '10$'
	else:
		cost = '15$'
	print ('your ticket cost is ', cost)