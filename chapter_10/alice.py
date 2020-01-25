#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 10

#The file 'alice.txt' does not exist, thus an exception will be raised. 
#It's then handled with an exception handler.
#To see the error handler in action remove the named 'alice.txt'


filename = 'alice.txt'

try:
	with open(filename, encoding= 'utf-8') as f:
		contents = f.read()
except FileNotFoundError:
	print(f"Apologies, the file {filename} does not exist.")
else:
	#Count the approximate number of words in the file.
	words = contents.split()
	num_words = len(words)
	print(f"The file {filename} has about {num_words} words.")


with open(filename, 'w') as f:
		f.write('Alice in wonderland')
#The split() function will build a list of words from a string.

#Project Gutenberg (http://gutenberg .org/) maintains a collection of literary works that
#are available in the public domain. It'll be useful for later projects