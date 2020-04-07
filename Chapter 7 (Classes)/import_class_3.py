from class_for_import_3 import Restaurant
restaurant = Restaurant("Cube", "King Georg, st, 3-14a")
restaurant.show_information()

from class_for_import_2_3 import Users, Priveleges, Admins
admins = Admins("Admin", "Admin", location = "Admin", sex = "Man")
admins.hello_user()
admins.describe_user()
admins.priveleges.show_priveleges()
admins.set_number_register_users(250)
admins.show_number_register_users()
