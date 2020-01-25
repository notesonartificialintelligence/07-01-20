#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 10

#Write a loop that asks people why they like programming.
#Each time someone enters a reason, add their reason to file that stores all the responses.

filename = 'response_poll.txt'


flag = True
count = 1

#While loop
while flag:

	prompt = "Tell me, why do you like programming? "
	response = input(prompt)

	#append to the file.
	with open(filename, 'a') as file_object:
		file_object.write(f"{response}\n")

	#Increment count
	count += 1

	#conditional test
	if count > 4:
		flag = False

#Read the file
with open(filename) as file_object:
	contents = file_object.read()

print(contents)




