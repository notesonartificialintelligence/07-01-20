#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 9


#Create three instances of the Restaurant class.
class Restaurant:
	def __init__(self, restaurant_name, cusine_type):
		self.restaurant_name = restaurant_name
		self.cusine_type = cusine_type

	def open_restaurant(self):
		"""Display a message"""
		print(f"The restaurant {self.restaurant_name.title()} is now open\n")

	def describe_restaurant(self):
		"""Print out the attributes of the class"""
		print(f"The restaurant in question is named: {self.restaurant_name.title()}.")
		print(f"The cusine of {self.restaurant_name.title()} is {self.cusine_type.title()}\n")


new_restaurant = Restaurant('Rannaghor', 'indian')
new_restaurant.describe_restaurant()

restaurant_01 = Restaurant('The Kitchen','British')
restaurant_01.describe_restaurant()

restaurant_02 = Restaurant('Beijing Buffet', 'Chinese')
restaurant_02.describe_restaurant()
