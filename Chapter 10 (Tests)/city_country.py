def city_country(city, country, population=''):
	if population:
		location = city + ", " + country + " - population " + str(population)
	else:
		location = city + ", " + country
	return location

