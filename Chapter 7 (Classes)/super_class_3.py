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

class IceCreamShop(Restaurant):
	
	def __init__(self, restaurant_name, restaurant_adress):
		super().__init__(restaurant_name, restaurant_adress)
		self.ice_cream_sort = 35
		
	def show_ice_cream_sort(self):
		print("We have " + str(self.ice_cream_sort) + " sorts of ice cream!")
		
ice_cream_shop = IceCreamShop("Wonderlaand Ice", "Lui Paster, st, 23-b")
ice_cream_shop.show_information()
ice_cream_shop.show_ice_cream_sort()
		
