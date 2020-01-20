#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 8
#Module

def make_pizza(size, *toppings):
	"""Summerise the pizza we're about to make."""
	print("\nMaking a {size}-inch pizza with the follow toppings: ")
	for topping in toppings:
		print(f" - {topping}")


