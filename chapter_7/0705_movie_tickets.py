#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 7

#Write a loop which will ask users for their age, and then tell them the sode of their movie ticket.

prompt = "Welcome to the ticket machine. Enter your age: "
prompt += "\nType 'Quit' to end program\n"

age = ""

while age.lower() != 'quit':

	age = input(prompt)

	#Casting the text into a string
	#age = int(age)

	if int(age) < 3:
		print('Your ticket will be free, enjoy')
	elif int(age) < 12:
		print('Your ticket will be $10.')
	elif int(age) >= 12:
		print('Your ticket will be $15')

