def display_message():
	print("Hi! I am a function!")
display_message()

def good_book(title):
	print("I am sure that good book is " + " '" + title.title() + "'.")
good_book("Origin")

def t_shirt(size = "L", text = "I love Python!"):
	print("This T-shirt have a such size: " + "'" + str(size) + "'" + " and such text: " + "'" + text + "'.")
t_shirt()
t_shirt(size = "M", text = "I love NASA!")

def describe_city(city, country = "England"):
	print(city + " is in " + country)
describe_city(city = 'Manchester')
describe_city(city = "London")
describe_city(city = 'Liverpool')

def singer_albom(singer, albom):
	dictionary = {"Name" : singer, "Name of albom" : albom}
	for k, v in dictionary.items():
		print(k + " : " + v)
singer_albom("T-Fest", "0372")

while True:
	name = input("Enter a name of singer: ")
	albom_name = input("Enter a name of albom: ")
	exit_programm = input("Exit? (Enter 'y or 'n'): ")
	if exit_programm == 'n':
		continue
	elif exit_programm == 'y':
		singer_albom(name, albom_name)
		break


