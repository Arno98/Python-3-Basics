users = ['admin', 'Sara', 'Tom', 'Mikle', 'Jesica', 'Katrin']
for user in users:
	if user == 'admin':
		print("Hello, admin, how are you?")
	else:
		print("Hello " + user)

if users:
	print("That is ok")
else:
	print("We need some users")
	
curent_users = ['Sara', 'Tom', 'Mikle', 'Jesica', 'Katrin']
new_users = ['John', 'Jack', 'Mikle', 'Tom', 'Albina', 'Karl', 'TOM', 'mikle']
for new_user in new_users:
	if new_user.title() in curent_users:
		print("Sorry but name "  + "'" + new_user + "'" + " uses. Try to write an other name.")
	else:
		print("Name " + "'" + new_user + "'" + " is free.")
		
numbers = list(range(1, 10))
for n in numbers:
	if n == 1:
		print(str(n) + "st")
	elif n == 2:
		print(str(n) + "nd")
	elif n == 3:
		print(str(n) + "rd")
	else:
		print(str(n) + "th")
		

