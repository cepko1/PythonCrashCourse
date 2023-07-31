pizzas = ['chorizzo', 'salyami', 'proshutto','quadroformadho', 'ananas']
for pizza in pizzas:
	print ( f'I like pizza {pizza}')
print('I like any pizza')
print('The first three items is', pizzas[:3])
print('The last three pizzas is', pizzas[-3:])
print('the midfle if pizzas is',pizzas[1:4])
newpizza = pizzas[:]
pizzas.append('corn')
newpizza.append('bacon')
print('there are two pizzacafe')
print('menu of first cafe is:')
for p in range(len(pizzas)):
	print(f'{p}: {pizzas[p]}')
print('\nin second cafe are such pizza')
for p in newpizza:
	print(f'{p}, ',end='  ')