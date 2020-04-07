human = {'head' : 1, 'hands' : 2, 'foot' : 2, 'eyes' : 2, 'nose' : 1}
print(human)

numbers = {'Ed' : 314, 'Saimon' : 7, 'Karl' : 27, 'Sara' : 8}
for n in numbers:
	print(n + " : " + str(numbers[n]))

glossary = {'python' : 'a programing language', 'biology' : 'a science about nature', 'mathematics' : 'a science about numbers'}
for g in glossary:
	print(g + " -- " + glossary[g])
	
for g in glossary:
	print(g + "\n" + glossary[g])
	
for key, value in glossary.items():
	print("\nKey : " + key)
	print("Value : " + value)
	
rivers = {'Nile' : 'Egypt', 'Dnipro' : 'Ukraine', 'Amazonka' : 'South America'}
for r, c in rivers.items():
	print("The " + r + " runs through " + c)
	
for r in rivers:
	print(r)
for r in rivers:
	print(rivers[r])
	
current_people = ['Tom', 'Any', 'Lucy', 'Edward']
new_people = ['Tom', 'Karl', 'Lucy', 'Edward']
for new in new_people:
	if new.title() in current_people:
		print("You have finished your asking")
	else:
		print("Can you tell about your favourite language ?")
		
interviewd_people = {'Tom' : 'Python', 'Edmond' : 'Python', 'Lucy' : 'C++'}
will_be_interviwed = ['Sara', 'Tom', 'Karl']
for name in will_be_interviwed:
	if name.title() in interviewd_people.keys():
		print("You have interviewed.")
	else:
		print("Can you tall about your favourite languages please ?")
	
	
