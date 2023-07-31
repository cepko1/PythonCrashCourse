from random import randint

size = 36 #size of lottery field from 1 to size
width = 5 #how many numbers in lottery ticket
numbers = []
n = 0
for i in range(width): #enter user numbers
	while True:
		n = int(input(f'Enter {i+1} number'))
		if n in numbers or not 0 < n <= size:
			print('plese enter other number')
		else:
			numbers.append(n)
			break

print(numbers)
a = input()#pause
count = 0
rand_n = []
while sorted(numbers) != sorted(rand_n):
	rand_n = []
	for i in range(width):
		while True:
			rnd = randint(1,size)
			if rnd in rand_n:
				continue
			else:
				rand_n.append(rnd)
				break
	count += 1
	print(rand_n)
print(f'Your combination found on {count} attempt')