car = input('Enter a car what do you want to choice ? ')
print("You choice a(an) " + car.title() + '.' + " This a brilliant choice!")

table = int(input('What time do you want table (from 8am to 23pm) ? '))
if table < 8:
	print("Sorry, Sir, but this time we are closed. Work time from 8 am to 23.pm")
if table >= 8 and table < 20:
	print("Ok.You choice an table in this time: " + str(table) + ".")
if table >= 20:
	print("Sorry, sir, but the tables in this time a busy.")
	
number_to_ten = int(input("Enter a number: "))
if number_to_ten / 10 == 0:
	print("OK")
else:
	print("NO")



