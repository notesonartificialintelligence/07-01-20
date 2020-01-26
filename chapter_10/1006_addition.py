#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 10

#Write a program that prompts users for two numbers. Add them together and print the result.
#catch the ValueError if either input is not a number.


first_number = input("First Number: ")

second_number = input("Second Number: ")


try:
	answer = int(first_number) + int(second_number)
except ValueError:
	print("Please enter two numerical values.")
else:
	print(answer)