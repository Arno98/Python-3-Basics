while True:
	try:
		a = int(input("Enter a number: "))
		b = int(input("Enter a number: "))
	except ValueError:
		print("You do not enter a number.Please try again.")
	else:
		print(a * b)
		exit_text = input("Do you want exit?(enter 'y' or 'n') ")
		if exit_text == 'n':
			continue
		elif exit_text == 'y':
			break
		else:
			print("You must enter 'y' or 'n'")
			
print("\n")
		
def file_function(filename):
	try:
		with open(filename) as filetext:
			read_file = filetext.read()
	except FileNotFoundError:
		print("The file " + "'" + filename + "'" + " is not found!")
	else:
		print(read_file.rstrip())
		words = read_file.split()
		numbers_of_words = len(words)
		print("'" + filename + "'" + " consist of " + str(numbers_of_words) + " words.")
		print("\n")
files = ["guest.txt", "guest_book.txt", "Learn Python.txt", "Wonderland.txt"]
for filename in files:
	file_function(filename)
