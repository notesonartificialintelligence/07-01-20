#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 7

#Write a program that polls users about their dream vacation.


vacation_poll = {}


flag = True

while flag:


#prompt for the person's name and response.
	prompt = "If you could visit a place in the world, where would you go?"

	name = input("What is your name?")

	response = input(prompt)
#Store the response in the dictionary.
	vacation_poll[name] = response
#Find out if anyone else is going to take the poll.
	repeat = input("Would you another person like to continue? (yes/no):")
	if repeat.lower() == 'no':
		flag = False



#Polling is complete. Show the results.
print("\n--- Poll Results ---")


for key, value in vacation_poll.items():
	print(f"{key}, would love to visit {value}")	
