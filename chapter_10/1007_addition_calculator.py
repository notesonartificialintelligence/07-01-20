#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 10

#Wrap the code from exercise 1006 in a while loop.
#And continue entering numbers even if they make a mistake and enter text 
#instead of a number.


while True:

	first_number = input("First Number: ")

	second_number = input("Second Number: ")

	try:
		answer = int(first_number) + int(second_number)
	except ValueError:
		pass
	else:
		print(answer)