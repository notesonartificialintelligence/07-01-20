#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 10

#The json function allows programs to store and load entered user data.
#The jason.dump() function takes two arguments: 
#a piece of data to store, and file object it can use to store the data.

#first import the json moudle
import json

numbers = [ 2, 3, 4, 5, 11, 13]

filename = "numbers.json"
with open(filename, 'w') as f:
	#The piece of data to store, and the file object to store the data onto.
	json.dump(numbers, f)

#The program number_reader.py then reads this text.