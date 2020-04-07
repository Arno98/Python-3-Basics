ingredients_of_pizza = ['tomato', 'meat', 'cucamber', 'cheese', 'fish', 'sousage']

print("This a first three ingredients of pizza: ")
for i in ingredients_of_pizza[:3]:
	print(i.title())

print("This a second two ingredients of pizza: ")
for i in ingredients_of_pizza[3:5]:
	print(i.title())
	
print("This a last ingredient of pizza: ")
for i in ingredients_of_pizza[5:]:
	print(i.title())
	
ingredients_of_my_pizza = ingredients_of_pizza[:]
ingredients_of_pizza.append('chicken')
ingredients_of_my_pizza.append('apple')
print("You pizza consist of ")
for i in ingredients_of_pizza:
	print("\t" + i.title())
print("My pizza consist of ")
for i in ingredients_of_my_pizza:
	print("\t" + i.title())
	
for i in ingredients_of_my_pizza:
	print(i.title())
print("---------")
for i in ingredients_of_pizza:
	print(i.title())
	

