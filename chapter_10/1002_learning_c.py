#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 10

#Use the funciton replace() to replace a word in the file with another
#Replace the word python with C


filename = 'learning_python.txt'

with open(filename) as file_object:
	for line in file_object.readlines():
		new_line = line.replace('Python', 'C')

		print(new_line)
