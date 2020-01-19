#Gabriel Abraham
#notesinartificialintelligence
#Python Crash Course - Chapter 8

#Positional Arguments

def describe_pet(animal_type, pet_name):
	"""Display information about a pet"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')
describe_pet('dog', 'willie')

#Key word arguments free you from having to worry about the order of the parameters.

describe_pet(animal_type = "hamster", pet_name = 'harry')

describe_pet(pet_name = 'harry', animal_type = "hamster")