#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 10

#Make two text files, cats and dogs. Store at least 3 names in each file
#Write a program that tried to read these files and print the contents of the file
#to the screen.

#This program will not cause an exception now, that is unless you remove the two required files.


cat_fileName = 'cats.txt'
dog_fileName = 'dogs.txt'


try:
	with open(cat_fileName) as cf:
		cat_contents = cf.read()

	with open(dog_fileName) as df:
		dog_contents = df.read()

except FileNotFoundError:
	print(f"Unfortunately, the file {cat_fileName}, cannot bt located.\n")
	print(f"Unfortunately, the file {dog_fileName}, cannot bt located.\n")
else:
	print(cat_contents + "\n")
	print(dog_contents)