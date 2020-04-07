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
