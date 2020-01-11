#Gabriel Abraham
#notesonartificialintelligence
#Make a list of the first 10 cube numbers, then use the for loop to print out the value of each cube.


#Using list comprehension.

cubed_list = [value ** 3 for value in range(1,11)]

for value in cubed_list:
	print(value)

print(f"Here's the full list: {cubed_list}")	