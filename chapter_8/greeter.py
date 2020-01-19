#Gabriel Abraham
#notesinartificialintelligence
#Python Crash Course - Chapter 8

#Creating a function that prints a greeting.

def greet_user(username):
	"""Disply a simple greeting.""" #A docstring, this describes what the function does.
	print(f"Hello, {username.title()}!")

greet_user('Jesse')