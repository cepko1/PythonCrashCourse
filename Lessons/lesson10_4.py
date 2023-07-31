filename = 'guest_book.txt'
inp = ' '
with open(filename, 'a') as guests:
	while inp != '':
		inp = input('Enter your name. For finish just press enter: ')
		guests.write(inp.title() + '\n')
print('Finish')