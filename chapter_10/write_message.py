#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 10

filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming.")

with open(filename) as file_object:
	contents = file_object.read()

print(contents)