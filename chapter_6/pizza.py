#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 6
#A list in a dictionary


#Store information about a pizza being ordered.


pizza = {
	'crust' : 'thick',
	'toppings' : ['mushroom', 'entra cheese'],	
	}

#Summarise the order.

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping.title())