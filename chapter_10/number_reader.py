#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 10

import json

filename = 'numbers.json'

#Open the file with a type alias
with open(filename) as f:
	#Store the contents of the file in the variable numbers.
	numbers = json.load(f)

print(numbers)