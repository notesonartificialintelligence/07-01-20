#Gabriel Abraham
#notesinartificialintelligence
#Python Crash Course - Chapter 8

def get_formatted_name(first_name, last_name, middle_name = " "):
	"""Return a full name, neatly formatted."""

	if middle_name:
		full_name = f"{first_name} {last_name} {middle_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()


#This is an infinite loop!


while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")

	f_name = input("First name: \n")

	if f_name == 'q':
		print('Goodbye')
		break

	l_name = input("Last name: \n")
	if l_name == 'q':
		print('Goodbye')
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print(f"\nHello, {formatted_name}!")



