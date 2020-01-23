#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 9

#Import a module from the Standard Library

from random import randint
#Make a class Die with one attribute called sides, which has a default value of 6.

class Die:
	"""A simple Die class."""
	def __init__(self,die = 6):
		"""Initilise the default die size to 6."""
		self.die = die

	def roll_die(self):
		"""Prints a random number between 1 and nd number of sides the die has."""
		random_value = randint(0,self.die)

		print(random_value)


#Make a 6, 10 and 20 sided die. Roll them 10 times each.
die_6 = Die()
die_10 = Die(10)
die_20 = Die(20)

print("Die 6\t")
for value in range(10):
	print(die_6.roll_die())

	
print("Die 10\t")
for value in range(10):
	print(die_10.roll_die())

	
print("Die 20\t")
for value in range(10):
	print(die_20.roll_die())
	