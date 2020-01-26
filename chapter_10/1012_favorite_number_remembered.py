#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 10
import json
#Combine the two previous execerises.
#If the file is already stored, report the favorite number to the user.
#If not prompt for the user's favorite number and store it in a file.
#Run the program twice to see that it words.
#It works.

def get_filename():

	filename = 'favorite_numberr.txt'

	return filename

def get_number():
	
	filename = get_filename()

	number = input("What is your favorite number? ")

	with open(filename,'w') as f:
		json.dump(number, f)

	print_number()


def print_number():

	filename = get_filename()

	try:
		with open(filename) as f:
			favorite_number = json.load(f)
	except FileNotFoundError: 
		get_number() 
	else:
		print(f"I know your favorite number, it's: {favorite_number}")


print_number()