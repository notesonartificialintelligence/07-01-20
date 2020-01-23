#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 9

#A Simple users class.

class Users:

	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def describe_user(self):
		"""Prints a summary of the user's information"""
		print(f"The name of the user in question is:{self.first_name}{self.last_name}.")
		print(f"the user in question is {self.age} years old.\n")

	def greet_user(self):
		"""A function to greet the user"""
		print(f"Hello, {self.first_name}\last_name")


