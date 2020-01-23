#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 9

#Make a list or tuple containing a series of 10 numbers and 5 letters.
#Randomly select four numbers of letters from the list and print a message
#saying that any ticket matching these four numbers or letters wins a prize.

from random import randint

numbers = [11,33,4,5,6,45,55,99,8,12,'d', 'de', 'tr','pf']

#The value that'll be used for the random number generator
#length - 1, otherwise random number will select element 14, and there is no 14, 
#as the list starts from 0 and end at 13
length = (len(numbers) - 1)


print("If you have matched the following value, you'll be tonights winner!!")
print("Tonights values are: ")

for value in range(5):
	random_number = randint(0, length)
	print(f"{numbers[random_number]}")