#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 7

#A program that ask the user how many seats they will require.
#If the value is over 8, tell them they'll have to wait for a seat.

people = input("How many people are in the group? ")
people = int(people)

if people <= 8:
	print("We'll just have to wait a few minutes for a table.")
else:
	print("The table is ready")