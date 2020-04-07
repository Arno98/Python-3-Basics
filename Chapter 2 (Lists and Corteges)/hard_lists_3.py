guests = ['Elon', 'Bill', 'Tony', 'Edmond', 'Peter']

for g in guests:
	print("Come on my party, " + g)
	
print(guests[1])

guests[1] = "Jim"

print(guests)

print ("Come on my party, " + guests[0])
print ("Come on my party, " + guests[1])
print ("Come on my party, " + guests[2])
print ("Come on my party, " + guests[3])
print ("Come on my party, " + guests[4])

print("Ok, i decided to invite more guests")
guests.insert(0, "Karl")
guests.insert(2, "Dan")
guests.append("Juval")
print(guests)

for g in guests:
	print("Come on my party, " + g)
	
print ("I decided thay i will invite only two guests on my party.")
	
guests.pop(0)
guests.pop(0)
guests.pop(0)
guests.pop(0)
guests.pop(2)
guests.pop(2)
print(guests)

for n in guests:
	print(n)
	
del guests[0]
del guests[0]
print(guests)




