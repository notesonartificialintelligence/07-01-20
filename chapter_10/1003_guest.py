#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 10

#Write a program that promts the user for their name. 
#When they respond, write their name to a file called guest.txt

filename = 'guest.txt'


user_name = input("What is your name? ")

with open(filename, 'w') as file_object:
	file_object.write(f"{user_name}")


with open(filename) as file_object:
	contents = file_object.read()

print(contents)
