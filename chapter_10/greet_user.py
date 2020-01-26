#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 10

import json

filename = 'username.json'

with open(filename) as f:
	#Load the contents of f.
	username = json.load(f)

	print(f"Welcome back, {username}!")
