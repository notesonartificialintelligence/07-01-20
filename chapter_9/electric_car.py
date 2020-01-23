#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 9

from car import Car

class Battery:
	"""A simple attempt to model a battery for an electric car."""

	def __init__(self, battery_size = 75):
		"""Initialise the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-KWh battery.")

	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315

		print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
	"""Represents aspects of a car, specific to electric vehicles."""

	def __init__(self, make, model, year):
		"""Initalise attributes of the parent class.
			Then initalise attributes specific to an electric car
		"""
		super().__init__(make,model,year)
		
		self.battery = Battery()
