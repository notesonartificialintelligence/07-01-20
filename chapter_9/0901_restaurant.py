#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 9

#Create a class called Restaurant, create two methods, and then test to ensure everything works.
class Restaurant:
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


new_restaurant = Restaurant('Rannaghor', 'indian')

print(new_restaurant.restaurant_name)
print(new_restaurant.cusine_type)
new_restaurant.open_restaurant()
new_restaurant.describe_restaurant()

