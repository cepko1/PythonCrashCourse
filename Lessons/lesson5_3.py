current_users = ['admin', 'Mike', 'Stan', 'Artur', 'Laura']
new_users = ['Gloria', 'stan', 'martin', 'Victoria', 'Poll', 'Admin']
lower_case_current =[]
for user in current_users:
	lower_case_current.append(user.lower())
for user in new_users:
	if user.lower() in lower_case_current:
		print(f'Username {user} is already used. Please choose other name')
	else:
		print(f'Wellcome {user}')