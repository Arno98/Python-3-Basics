class Restaurant():
	
	def __init__(self, restaurant_name, restaurant_adress):
		self.restaurant_name = restaurant_name
		self.restaurant_adress = restaurant_adress
		
	def show_information(self):
		print("My restaurant is " + "'" + self.restaurant_name + "'.")
		print("My restaurant is situated on this adress: " + self.restaurant_adress)
		
restaurant = Restaurant("Place", "Oliver Cromvell, st, 27-a")
restaurant.show_information()

print("\n")

class Users():
	
	def __init__(self, first_name, last_name, **others_data):
		self.first_name = first_name
		self.last_name = last_name
		self.others_data = others_data
		self.number_register_users = 0
		
	def hello_user(self):
		print("Hello, " + self.first_name + " " + self.last_name)
		
	def describe_user(self):
		print("Your data:")
		user_data = {"Name" : self.first_name, "Last Name" : self.last_name}
		for key, value in self.others_data.items():
			user_data[key] = value
		for k, v in user_data.items():
			print("\t" + k + " : " + v)
			
	def set_number_register_users(self, users_accounts):
		self.number_register_users = users_accounts
		
	def update_users(self, new_users):
		self.number_register_users += new_users
		print(str(new_users) + " new users registered on site today.")
			
	def show_number_register_users(self):
		print("On site register " + str(self.number_register_users) + " accounts.")
	
			
users = Users("Jack", "Simpson", age = "25", profession = "Programmer", status = "Alone")
users.hello_user()
users.describe_user()
users.show_number_register_users()

users.set_number_register_users(7567)
users.show_number_register_users()

users.update_users(100)
users.show_number_register_users()

users.set_number_register_users(12897)
users.update_users(200)
users.show_number_register_users()

print("\n")

class PlusOne():
	
	def __init__(self):
		self.variable = 0
	
	def plus_one(self):
		self.variable += 1
		
	def reset_variable(self):
		self.variable = 0
		
plusone = PlusOne()
print(plusone.variable)
plusone.plus_one()
plusone.plus_one()
plusone.plus_one()
print(plusone.variable)
plusone.reset_variable()
print(plusone.variable)











