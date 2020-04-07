import unittest

from city_country import city_country

class TestLocation(unittest.TestCase):
	
	def test_location(self):
		location = city_country("Manchester", "England")
		self.assertEqual(location, "Manchester, England")
		
	def test_location_population(self):
		location = city_country("Manchester", "England", population=100000)
		self.assertEqual(location, "Manchester, England - population 100000")
		
unittest.main()




