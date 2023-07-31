from random import choice

letters =('a', 'b', 'c', 'd', 'e')
numbers = tuple((i + 1 for i in range(10)))
randomserial = choice(letters) + choice(letters) + str(choice(numbers)) + str(choice(numbers)) + str(choice(numbers)) + str(choice(numbers))
print(randomserial)