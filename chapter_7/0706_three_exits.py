#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 7

#Do the previous ending with three different exits:

#Use a conditional test in the while statement to stop the loop.

#Use an active variable to control how long the loop runs.

#Use a break statement to exit the loop when the user enters a 'quit' value.


#Use a conditional test in the while statement to stop the loop.
prompt = "Welcome to the ticket machine. Enter your age: "
prompt += "\nType 'Quit' to end program\n"

age = ""

flag = True

while flag:

	age = input(prompt)


	if age.lower() == 'quit':
		flag = False
	else:
		if int(age) < 3:
			print('Your ticket will be free, enjoy')
		elif int(age) < 12:
			print('Your ticket will be $10.')
		elif int(age) >= 12:
			print('Your ticket will be $15')



#Use an active variable to control how long the loop runs.

prompt = "Welcome to the ticket machine. Enter your age: "


age_2 = ""

current_number = 0

while current_number < 10:

	age_2 = input(prompt)

	#Casting the text into a string

	if int(age_2) < 3:
		print('Your ticket will be free, enjoy')
	elif int(age_2) < 12:
		print('Your ticket will be $10.')
	elif int(age_2) >= 12:
		print('Your ticket will be $15')

	current_number +=1


#Use a break statement to exit the loop when the user enters a 'quit' value.
prompt = "Welcome to the ticket machine. Enter your age: "
prompt += "\nType 'Quit' to end program\n"

age_1 = ""

flag = True

while flag:

	age_1 = input(prompt)

	#Casting the text into a string
	#age = int(age)

	if age_1.lower() == 'quit':
		break
	else:
		if int(age_1) < 3:
			print('Your ticket will be free, enjoy')
		elif int(age_1) < 12:
			print('Your ticket will be $10.')
		elif int(age_1) >= 12:
			print('Your ticket will be $15')

