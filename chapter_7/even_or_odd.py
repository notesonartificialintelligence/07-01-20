#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 7

#Using the module operator.
#Finding out if a number is odd or even.
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
	print(f"\nThe number {number} is even.")
else:
	print(f"\nThe number {number} is odd.")

print(number % 2)