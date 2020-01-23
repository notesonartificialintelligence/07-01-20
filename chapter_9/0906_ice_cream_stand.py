#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 9

#Write a new class that inherits from the Restaurant class.

#Create a class called Restaurant, create two methods, and then test to ensure everything works.
class Restaurant:
	"""A Simple Restaurant class"""
	def __init__(self, restaurant_name, cusine_type):
		self.restaurant_name = restaurant_name
		self.cusine_type = cusine_type

	def open_restaurant(self):
		"""Display a message"""
		print(f"The restaurant {self.restaurant_name.title()} is now open")

	def describe_restaurant(self):
		"""Print out the attributes of the class"""
		print(f"The restaurant in question is named: {self.restaurant_name.title()}.")
		print(f"The cusine of {self.restaurant_name.title()} is {self.cusine_type.title()}")


class IceCreamStand(Restaurant):
	"""A simple restaurant class."""
	def __init__(self,restaurant_name, cusine_type):
		"""Initalise attributes of the parent class.
			Then initalise attributes specific to an electric car
		"""
		super().__init__(restaurant_name, cusine_type)

		#Add an attribute called flavors
		self.flavors = ['cherry', 'banana', 'mint', 'chocolate']

	#Print the flovors in the list
	def show_flavor(self):
		print("The available flavors are: \n")

		for flavor in self.flavors:
			print("\t" + flavor.title())
		print(f"")



#Create an instance of IceCreamStand, and call this method.
new_stand = IceCreamStand('Ranaaghor', 'indian')

new_stand.show_flavor()
new_stand.describe_restaurant()