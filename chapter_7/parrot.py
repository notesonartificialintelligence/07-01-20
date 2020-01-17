#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 7

#Receiving text from the user: the input() funciton.

#The text in the input() function will prompt the user with what to do.

prompt = "Tell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True

message = ""

while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)

#The variable message is then assigned to the entered message.
#The message is then printed.