#Gabriel Abraham
#notesonartificialintelligence
#Make a list of the multiples of 3 - 30. Use a for loop to pring the numbers in your list.

#Not using list comprehension.
threes_list = []

for numbers in range(3,31,3): 	# I've used "numbers" instead of "value".
	print(numbers)
	threes_list.append(numbers)

print(f"Here is the full list: {threes_list}")