#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 10

import json

#Before printing a welcome back message in greet_user(), ask the user if
#this is the corrent username. If it's not, call get_new_username()
#to get the corrrect username.

#Load the username, if it had been stored previously.
#Otherwise, prompt for the username and store it.

def get_stored_username():
	"""Get stored unsername if available."""

	filename = 'username.json'

	try:
		with open(filename) as f:
			#Store the user entered data into the file f
			username = json.load(f)

	except FileNotFoundError:
		return None

	else:
		return username

def get_new_username():
	"""Prompt for a new username."""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f:
		json.dump(username, f)
		return username


def greet_user(verfied_name):
	"""Greet the user by name."""

	username = verfied_name

	print(f"Welcome back, {username}! ")


def verify_user():

	username = get_stored_username()

	if username:
		print(f"Are you, {username}")
		confirmation = input("Yes or No?\n")

		if confirmation.lower() == 'yes':
			greet_user(username)
		else:
			username = get_new_username()
			print(f"We'll remember you when you come back, {username}!")
	else:
		username = get_new_username()
		


verify_user()