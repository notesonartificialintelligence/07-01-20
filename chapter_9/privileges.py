#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 9

#A simple privileges class

class Privileges:

	def __init__(self):
		self.privileges = ['can add post', 'can delete post', 'can ban user']

	def show_privileges(self):
		"""Print out the privileges of the user."""
		print("These are the current privileges of the Administrator: ")

		for privilege in self.privileges:
			print(privilege.title())