if 2 == (4 - 2):
	print(True)
else:
	print(False)

if 23 != (11 + 11):
	print(True)
else:
	print(False)
	
answer = input("Enter the name of the car in lower() function: ")
if answer != answer.lower():
	print('Enter the name of car in lower function!')
else:
	print("That is all right!")

answer_two = input("Enter a name: ")	
list_of_guest = ['Bill', 'Tony', 'Elon', 'Karl']
if answer_two.title() in list_of_guest:
	print("OK!")
else:
	print("Wrong!")
	
if 'Jack' not in list_of_guest:
	print("I am sorry but you outside this list.")
else:
	print("OK")

