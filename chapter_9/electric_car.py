#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 9

class Car:
	"""A simple attempt represent a car."""

	def __init__(self,make,model,year):
		"""Initalise attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		"""Set the odometer reading to the given value.
			Rejec the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		"""Ade the given amount to the odometer reading."""
		self.odometer_reading += miles

class ElectricCar(Car):
	"""Represents aspects of a car, specific to electric vehicles."""

	def __init__(self, make, model, year):
		"""Initalise attributes of the parent class.
			Then initalise attributes specific to an electric car
		"""
		super().__init__(make,model,year)
		
		self.battery_size = 75

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-KWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()