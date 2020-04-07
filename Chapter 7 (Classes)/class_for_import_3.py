class Restaurant():
	
	def __init__(self, restaurant_name, restaurant_adress):
		self.restaurant_name = restaurant_name
		self.restaurant_adress = restaurant_adress
		
	def show_information(self):
		print("My restaurant is " + "'" + self.restaurant_name + "'.")
		print("My restaurant is situated on this adress: " + self.restaurant_adress)
		
restaurant = Restaurant("Place", "Oliver Cromvell, st, 27-a")
restaurant.show_information()

