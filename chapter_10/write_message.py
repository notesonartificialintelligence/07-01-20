#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 10

filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")



#Appending to a file
with open(filename, 'a') as file_object:
	file_object.write("I aso love finding meaning in large datasets.\n")
	file_object.write("I love creating apps the can run in a browser.\n")
with open(filename) as file_object:
	contents = file_object.read()

print(contents)