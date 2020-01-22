#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 9

#The attributes will be information
#The classes will be behaviours

class Dog:
	"""A simple attempt to model a god."""

	def __init__(self, name,age):
		"""Initialise name and age atrributes."""
		self.name = name
		self.age = age

	def sit(self):
		"""SImulate a dog sitting in response to a connant."""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in sesponse to a command."""
		print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)
your_dog = Dog("Lucy", 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is  {your_dog.name}.")
print(f"\nYour dog is {your_dog.age} years old.")
your_dog.sit()

