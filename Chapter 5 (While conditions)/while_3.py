pizza = []
flag = True
while flag:
	question = input("Enter an ingredients for your pizza(enter 'quit' to exit): ")
	if question != 'quit':
		pizza.append(question)
	else:
		print("Your ingredients:")
		print(pizza)
			
age_ticket = input("Enter your age: ")
if int(age_ticket) < 3:
	print("Free ticket!")
elif int(age_ticket) >= 3 and int(age_ticket) <= 12:
	print("10 dollars")
elif int(age_ticket) > 12:
	print("20 dollars")
	
stats = True
if stats:	
	enter_a_word = input("Enter a word(enter 'exit' to exit): ")
	if enter_a_word != 'exit':
		print(enter_a_word)
	while enter_a_word == 'exit':
		print("Exit!")
		stats = False
		break
		
while True:
	q = input("Enter a favorite book(enter 'quit' to exite): ")
	if q != 'quit':
		print(q)
	if q == 'quit':
		break

	

	
