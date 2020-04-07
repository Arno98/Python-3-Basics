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

class Priveleges():
	
	def __init__(self):
		self.priveleges = ["can ban users", "can write a statistic data", "can ban groups and others comunity"]
	
	def show_priveleges(self):
		print("Admins have a some priveleges:")
		for p in self.priveleges:
			print("\t" + "-" + p)

class Admins(Users):
	
	def __init__(self, first_name, last_name, **others_data):
		super().__init__(first_name, last_name, **others_data)
		self.priveleges = Priveleges()
			
admins = Admins("Admin", "Admin", age = "None", proffesion = "Admin", status = "Admin")
admins.hello_user()
admins.describe_user()
admins.priveleges.show_priveleges()
admins.set_number_register_users(100)
admins.show_number_register_users()
