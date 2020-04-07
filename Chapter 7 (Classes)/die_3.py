from random import randint
from time import sleep

class Die():
	
	def __init__(self, sides=6):
		self.sides = sides
		
	def roll_die(self):
		count_of_roll = 10
		while count_of_roll > 0:
			print("Rolling Die...")
			sleep(1)
			roll = randint(1, self.sides)
			print(str(roll))
			count_of_roll -= 1

die = Die()
die.roll_die()

		
