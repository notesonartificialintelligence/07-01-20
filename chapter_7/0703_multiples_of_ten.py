#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 7

#Ask the user for a number, and then report whether the number is a multiple of 10 or not.

#A prompt that will spread over 2 lines.
prompt = "I can calculate multiples."
prompt += "\nEnter a number, and I'll tell you if is a multiple of 10 "

number = input(prompt)

number = int(number)

if number % 10 == 0:
	print(f"\n {number}, is a multiple of 10")
else:
	print(f"\n {number}, is not a multiple of 10")