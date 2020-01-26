#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 10

import json
#Write a program that prompts for the user's favorite number.
#Use json.dump() to store this number in a file
#write a separate program that reads in this value.

#The seperate file is program is called '1011_seperate_file.py'

number = input("What is your favorite number? ")

filename = 'favorite_number.txt'

with open(filename,'w') as f:
	json.dump(number, f)