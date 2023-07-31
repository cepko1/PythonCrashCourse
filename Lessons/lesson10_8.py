def read_file(filename):
	try:
		with open(filename) as f:
			content = f.readlines()
	except FileNotFoundError:
		print(f"File '{filename}'does not exist")
	else:
		for line in content:
			print(line, end = '')
		
		
file_1 = 'lesson2_1.py'
file_2 = 'lesson8_4.py'
read_file(file_1)
read_file(file_2)