class Employee():
	
	def __init__(self, name, last_name, money):
		self.name = name
		self.last_name = last_name
		self.money = money
		
	def give_raise(self, money_plus=5000):
		self.money += money_plus
		return self.money
