#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 10

#Learning how to work with files, that way our programs will be able to quickly analyze lots of data.
#Also learning how to handle errors.

#Reading from a file.

#The open funciton is used to open a file. It takes in one argument.
filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())



#Reading line by line.