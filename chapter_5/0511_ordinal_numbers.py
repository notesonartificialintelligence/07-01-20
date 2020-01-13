#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 5

#Store the numbers 1 thorugh 9 in a list
numbers = [value for value in range(1,10)]

#Loop through that list.

for number in numbers:
	if number > 3:
		print(f"{number}th\n")
	elif number == 1:
		print(f"{number}st\n")
	elif number == 2:
		print(f"{number}nd\n")
	else:
		print(f"{number}rd\n")
