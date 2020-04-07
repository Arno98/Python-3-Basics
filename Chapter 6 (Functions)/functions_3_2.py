magicians = ['Dambldor', 'Volandemort', 'Harry Potter', 'Germiona']

def show_magicians(magicians):
	for magician in magicians:
		print(magician)
		
def great_magicians(magicians):
	great_magicians = []
	while magicians:
		magician = magicians.pop()
		magician_great = magician + " The Great!"
		great_magicians.append(magician_great)
	for magician_great in great_magicians:
		magicians.append(magician_great)

show_magicians(magicians)

print("\n")

great_magicians(magicians)
show_magicians(magicians)


def sandwiches(*ingredients):
	print('\nYour ingredients: ')
	for i in ingredients:
		print("\t" + "-" + i)
	print("\nYour sendwich is finished!")
sandwiches('tuna', 'cheese', 'potato', 'sousage', 'chicken', 'carry')
sandwiches('tomato', 'cucamber', 'nuts', 'bread', 'meat')

print("__________________")
print("\n")

def build_profile(name, last_name, **others_data):
	profile = {}
	profile["Name"] = name.title()
	profile["Last name"] = last_name.title()
	for key, value in others_data.items():
		profile[key] = value
	print(profile)
build_profile("John", "Brown", age = "37", location = "USA", proffesion = "Robotechiks, programmer, genius")

print("\n")

def car_complictation(name, model, color = "Black", package = False, **others_data_car):
	car = {}
	car["Name"] = name.title()
	car["Model"] = model.title()
	car["Color"] = color.title()
	car["Package"] = package
	for k, v in others_data_car.items():
		car[k] = v
	for key, value in car.items():
		print(str(key.title()) + " : " + str(value))
car_complictation("Bmw", "X6", color = "Green", package = True, Automat = "True", Cruiz_Control = "True", Neon  = "True")
		
print("\n")	
		
while True:
	car_name = input("Enter a car name: ")
	car_model = input("Enter a car model: ")
	car_color = input("Enter a car color: ")
	car_package = input("Enter a package(True / False): ")
	others_data = input("Do you want enter another data?(enter 'y' or 'n') ")
	if others_data == 'n':
		car_complictation(car_name, car_model, color = car_color, package = car_package)
		break
	elif others_data == 'y':
		car_automat = input("Do you want an automat?(enter True or False) ")
		car_cruiz_control = input("Do you want a cruiz control? (enter True or False) ")
		car_neon = input("Do you want a neon? (entre True or False) ")
		car_exit = input("Exit? (enter 'y' or 'n') ")
		if car_exit == 'y':
			car_complictation(car_name, car_model, color = car_color, package = car_package, Automat = car_automat, Cruiz_Control = car_cruiz_control, Neon = car_neon)
			break
		elif car_exit == 'n':
			print("We ended our car complictation!")
			break
			
		
	


	
	







