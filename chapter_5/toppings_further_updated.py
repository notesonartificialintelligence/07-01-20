#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 5

#requested_toppings = ["mushrooms","green peppers","extra cheese"]

requested_toppings = []

#When the name of a list is used in an if statement, if the list is empty python will interpret the list as false.
if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"{requested_topping.title()}, has been added to your pizza")
	print("\nYour pizza is ready.\n")
else:
	print("Are you sure you want a plain pizza?")



