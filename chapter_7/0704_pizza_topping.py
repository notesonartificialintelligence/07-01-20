#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 7

#Write a loop that promptsthe user to enter a series of pizza toppings until they enter
#a 'quit' value.

prompt = "Enter your pizza toppings."
prompt += "\nPress 'quit' to exit."

topping = ""

while topping.lower() != "quit":

	print(topping)

	topping = input(prompt)