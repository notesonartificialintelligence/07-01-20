#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 5

#Checking whether a value is not in a list.

banned_users = ["andrew","carolina","david"]
user = "marie"

if user not in banned_users:
	print(f"{user.title()}, my dear, you can post a response if you wish.")

#Checkings if a value is in a list.

user_1 = "andrew"

if user_1 in banned_users:
	print(f"{user_1.title()}, unfortunately, you've used up all of your chances. Your're banned.")