import json

def sciences(data_of_sciences):
	try:
		with open(data_of_sciences) as file_sciences:
			load_sciences = json.load(file_sciences)
	except FileNotFoundError:
		print("Sorry, this file is not exist. Enter your favorite sciences and we will creat your file.")
		with open(data_sciences, 'w') as file_sciences:
			love_sciences = input("Enter your favorite sciences: ")
			json.dump(love_sciences, file_sciences)
	else:
		print(load_sciences)
		
filename = "Sciences.json"
sciences(filename)


	

