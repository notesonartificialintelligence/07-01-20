#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 5

#Write code to greet each user as though they were signing into a website.
#The admin is asked if they want to see a status report


usernames = []

#Similar to the previous task, but, add an if statement to ensure that the list is not empty.
if usernames:
	for username in usernames:
		if username.lower() == "admin":
			print("Hello Admin, would you want to see a status report.")
		else:
			print(f"Hello {username}, thank you for logging in again.")	
else:
	print("We'll need to find some users!")