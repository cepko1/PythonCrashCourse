sandwich_order = {}
working = True
while working:
	sandwich = input('Please enter title for your sandwich (if you wanna stop enter"stop": ')
	if sandwich == 'stop' : break
	ingredients = []
	ingr = ' '
	while ingr:
		ingr = input('Please enter your ingredint (if you wanna stop just press enter)')
		if not ingr:
			continue
		else:
			ingredients.append(ingr)
	sandwich_order[sandwich] = ingredients
for title, ingrs in sandwich_order.items():
	print(f'Sandwich {title} consist of:', end = (' '))
	for ingr in ingrs:
		print(ingr, end = ' ')
	print()