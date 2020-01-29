#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 11

class Employee():
	"""A simple Employee class."""

	def __init__(self,first, name, salary):
		"""Initiate the attributes."""
		self.first = first
		self.name = name
		self.salary = int(salary)

	def give_raise(self,raise_amount = "1000"):
		
		self.salary += int(raise_amount)
