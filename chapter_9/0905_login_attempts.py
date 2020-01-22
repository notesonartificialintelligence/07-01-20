#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 9

#Modify the class below.
class Users:

	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		#Add an attribute login_attempts
		self.login_attempts = 0

	def describe_user(self):
		"""Prints a summary of the user's information"""
		print(f"The name of the user in question is:{self.first_name}{self.last_name}.")
		print(f"the user in question is {self.age} years old.\n")

	def greet_user(self):
		"""A function to greet the user"""
		print(f"Hello, {self.first_name}\last_name")

	#Create a new funtion that increments the login attempts
	def increment_login_attempts(self):
		"""Increment the attribute login_attempts"""
		self.login_attempts += 1

	#Create a function that resets the number of login attempts
	def reset_login_attempts(self):
		"""Reset the number of login attempts"""
		self.login_attempts = 0
		reset_output = f"The login attampts have been reset,\n"
		reset_output += f"the value is now {self.login_attempts}.\n"

		return reset_output



gabriel = Users('gabriel','abraham', 24)
gabriel.describe_user()
gabriel.greet_user()

#For loop to increase the login attempts
for value in range(5):
	gabriel.increment_login_attempts()

print(gabriel.login_attempts)
print(gabriel.reset_login_attempts())


james = Users('James', 'Adam', 35)
james.describe_user()
james.greet_user()

charles = Users('charles', 'time', 23)
charles.describe_user()
charles.greet_user()