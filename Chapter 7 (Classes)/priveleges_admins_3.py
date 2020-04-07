from users_class_3 import Users

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
			
admins = Admins("Admin", "Admin")
admins.hello_user()
admins.priveleges.show_priveleges()

