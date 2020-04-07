try:
	print(10 / 0)
except ZeroDivisionError:
	print("You can not divide by zero!")

print("\n")
	
question = input("Enter a number: ")
try:
	number = int(question)
except ValueError:
	print("You can enter only a number!")
else:
	print(number)

print("\n")

file_book = "The Farm.txt"
try:	
	with open(file_book) as book:
		book.read()
except FileNotFoundError:
	print("Sorry, but the file " + "'" + file_book + "'" + " does not exist.")
	
print("\n")
	
file_work = "Student Work.txt"
try:
	with open(file_work) as student_work:
		work_read = student_work.read()
except FileNotFoundError:
	print("Sorry, but the file " + "'" + file_work + "'" + " does nor exist.")
else:
	words = work_read.split()
	number_of_words = len(words)
	number_of_getman = words.count('гетьман')
	print("The file " + "'" + file_work + "'" + " has about " + str(number_of_words) + " words.")
	print("Word " + "'гетьман'" + " was writen about " + str(number_of_getman))
	
