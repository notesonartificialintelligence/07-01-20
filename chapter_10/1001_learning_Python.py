#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 10

#Write a program that reads the file and prints what has been written 3 times.
#Print the list once by reading in the entire file.
#Once by looping over the file object
#Once by storing the lines in a list and then working with them outside the with block.

filename = 'learning_python.txt'

#Print the list once by reading in the entire file.
with open(filename) as file_object:
	contents = file_object.read()

print(contents)

#Once by looping over the file object
with open(filename) as file_object:
	for line in file_object:
		print(line)


#Once by storing the lines in a list and then working with them outside the with block.
with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line)