#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 9

#Write a class admin that inherits from the user class.

class Users:
	"""A simple user class."""
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def describe_user(self):
		"""Prints a summary of the user's information"""
		print(f"The name of the user in question is: {self.first_name.title()} {self.last_name.title()}.")
		print(f"the user in question is {self.age} years old.\n")

	def greet_user(self):
		"""A function to greet the user"""
		print(f"Hello, {self.first_name}\last_name")


class Admin(Users):
	"""A simple admin class"""
	def __init__(self, first_name, last_name, age):
		"""Initialise attributes of the parent class."""
		super().__init__(first_name, last_name, age)

		#Add attribute privileges, that stores a list of string like: 'can add post'...
		#Add a function that will list the administrators set of privileges.
		self.privileges = Privileges()


class Privileges:

	def __init__(self):
		self.privileges = ['can add post', 'can delete post', 'can ban user']

	def show_privileges(self):
		"""Print out the privileges of the user."""
		print("These are the current privileges of the Administrator: ")

		for privilege in self.privileges:
			print(privilege.title())

