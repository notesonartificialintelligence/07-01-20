#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 9

#Write a class admin that inherits from the user class.
from users import Users 
from privileges import Privileges

class Admin(Users):
	"""A simple admin class"""
	def __init__(self, first_name, last_name, age):
		"""Initialise attributes of the parent class."""
		super().__init__(first_name, last_name, age)

		#Add attribute privileges, that stores a list of string like: 'can add post'...
		#Add a function that will list the administrators set of privileges.
		self.privileges = Privileges()




