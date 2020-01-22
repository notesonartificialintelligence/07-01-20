#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 9

#Start with the below class, and add a few changes.
class Restaurant:
	"""A Simple Restaurant class"""
	def __init__(self, restaurant_name, cusine_type):
		self.restaurant_name = restaurant_name
		self.cusine_type = cusine_type
		#Added attribute
		self.number_served = 0

	def open_restaurant(self):
		"""Display a message"""
		print(f"The restaurant {self.restaurant_name.title()} is now open")

	def describe_restaurant(self):
		"""Print out the attributes of the class"""
		print(f"The restaurant in question is named: {self.restaurant_name.title()}.")
		print(f"The cusine of {self.restaurant_name.title()} is {self.cusine_type.title()}")

	#Add the method below
	def set_number_served(self, number):
		"""Set the number of customers that have been served."""
		self.number_served = number

		return self.number_served

	#Add the method below
	def increment_number_served(self):
		"""Increment the number of people served
		I'll increment it by 1"""
		self.number_served += 1

new_restaurant = Restaurant('rannaghor', 'indian')

new_restaurant.set_number_served(23)

print(new_restaurant.number_served)

new_restaurant.increment_number_served()

print(new_restaurant.number_served)