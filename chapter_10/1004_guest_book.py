#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 10

#Write a loop that prompts users for their name. When they've entered their name, print a greeting
#and add a line recording their visit in a file called guest_book.txt
#Ensure that each entry appears on a new line in the file.


flag = True

filename = 'guest_book.txt'

#Create the file, and enter the title.
with open(filename,'w') as file_object:
	file_object.write("Guest Book\n")


count = 1
flag = True

#While loop to ask for input.
while flag:
	name = input("What is your name? ")
	greeting = f"Hi {name}, have fun."

	#append the names onto the file.
	with open(filename,'a') as file_object:
		file_object.write(f"{name}\n")

	count += 1

	if count > 3:

		flag = False


#Print the the entries in the file one by one
with open(filename) as file_object:
	for lines in file_object.readlines():
		print(lines)