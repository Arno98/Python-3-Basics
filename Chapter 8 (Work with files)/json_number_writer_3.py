import json

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

number_file = "number_writer.json"
with open(number_file, 'w') as file_object:
	json.dump(numbers, file_object)
