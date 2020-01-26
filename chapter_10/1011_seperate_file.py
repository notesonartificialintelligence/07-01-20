#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 10

import json

filename = 'favorite_number.txt'

with open(filename) as f:
	favorite_number = json.load(f)

print(f"I know your favorite number, it's: {favorite_number}")