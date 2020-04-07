print("We do not have a pastrami sandwich!")
sandwich_orders = ['tuna sandwich', 'cheese sandwich', 'chicken sandwich', 'tomato sandwich', 'pastrami sandwich']
finished_sandwich = []
for sandwich in sandwich_orders:
	while 'pastrami sandwich' in sandwich_orders:
		sandwich_orders.remove('pastrami sandwich')
	print("I made your " + sandwich)
	finished_sandwich.append(sandwich)

print("Your finished sandwiches:")
for sandwich in finished_sandwich:
	print("\t" + sandwich)
	
trip = []	
while True:
	name_question = input("What is your name ? ")
	trip.append(name_question)
	
	country_question = input("Hello, " + name_question.title() + ", what country do you want to visit ? ")
	trip.append(country_question)
	
	kind_of_transport = input(country_question.title() + " is a great choose! What kind of transport do you prefer ? ")
	trip.append(kind_of_transport)
	
	print("Ok. We save your data!")
	y_or_n = input("Do you want exit ?(enter 'y' or 'n') ")
	if y_or_n == 'n':
		trip.remove(name_question)
		trip.remove(country_question)
		trip.remove(kind_of_transport)
		continue
	elif y_or_n == 'y':
		print("\t" + "-----Results-----")
		print("Name : " + trip[0].title())
		print("Country to visit : " + trip[1].title())
		print("Kind of transport : " + trip[2].title())
		print("Thanks for the answers!")
		break

print("-------Poll with dictoinaries-------")
		
trip = {}	
while True:
	name_question = input("What is your name, sir/madam ? ")
	trip["Name"] = name_question
	
	country_question = input("Hello, " + name_question.title() + ", what country do you want to visit ? ")
	trip["Country to visit"] = country_question
	
	kind_of_transport = input(country_question.title() + " is a great choose! What kind of transport do you prefer ? ")
	trip["Kind of transport"] = kind_of_transport
	
	print("Ok. We save your data!")
	y_or_n = input("Do you want exit ?(enter 'y' or 'n') ")
	if y_or_n == 'n':
		del trip["Name"]
		del trip["Country to visit"]
		del trip["Kind of transport"]
		continue
	elif y_or_n == 'y':
		print("\t" + "-----Results-----")
		for k, v in trip.items():
			print(k + " : " + v.title())
		break
        
