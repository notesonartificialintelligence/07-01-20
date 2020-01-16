#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 6

favorite_numbers = {
		'james': [6],
		'George': [55, 3],
		'Gabriel': [89, 43],
		'Maria': [19,12],
		'Emmanuel': [44,55],
	}

for name, numbers in favorite_numbers.items():
		if len(numbers) > 1:
			print(f"{name} has multiple favorite numbers, and they are: ")

			for number in numbers:
				print(f"{number}" )
		else:
			for number in numbers:
				print(f"{name.title()} has a favorite number, and its: {number}")