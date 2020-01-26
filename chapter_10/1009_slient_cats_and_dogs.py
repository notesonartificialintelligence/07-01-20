#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 10

#Modify the except block in the previous exercise to fail silently.

#This program will cause a silent exception, The file 'dogsss.txt' does not exist.


cat_fileName = 'cats.txt'
dog_fileName = 'dogsss.txt'


try:
	with open(cat_fileName) as cf:
		cat_contents = cf.read()

	with open(dog_fileName) as df:
		dog_contents = df.read()

except FileNotFoundError:
	pass
else:
	print(cat_contents + "\n")
	print(dog_contents)