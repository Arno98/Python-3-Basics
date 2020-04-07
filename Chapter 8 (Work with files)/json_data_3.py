import json

def stored_name():
	data_name = "Data File.json"
	try:
		with open(data_name) as save_name:
			save_user_name = json.load(save_name)
	except FileNotFoundError:
		None
	else:
		return save_user_name
		
def show_name():
	save_user_name = stored_name()
	question_about_name = input("Your name is " + "'" + save_user_name + "'" + "? (enter 'y' or 'n') ")
	if question_about_name == 'y':
		print("Hello, " + save_user_name + "!")
	elif question_about_name == 'n':
		new_name()
		
def new_name():
	data_name = "Data File.json"
	name = input("Please, enter your name: ")
	with open(data_name, 'w') as new_user_name:
		json.dump(name, new_user_name)
		print("Ok, " + name + ", we saved your name.")
		
show_name()
	
		
