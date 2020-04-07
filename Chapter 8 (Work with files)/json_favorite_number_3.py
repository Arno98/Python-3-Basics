import json

number = input("Enter your favorite number: ")
file_number = "love_number.json"
with open(file_number, 'w') as file_object_number:
	json.dump(number, file_object_number)
	

