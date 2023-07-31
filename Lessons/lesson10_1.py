filename = 'lesson9_2.py'
with open(filename) as workfile:
	data = workfile.read()
print('All solid file')
print(data)
filename = 'lesson4_2.py'
with open(filename) as workfile:
	lines = workfile.readlines()
print('Reading file as list of lines')
print(lines)
print('Cycle by lines:')
for line in lines:
	print(line.strip())