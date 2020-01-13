#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 5

user = "andrew"
banned_users = ["andrew","carolina","david\n"]

print("Is 'andrew' banned? I predict true.\n")

if user.lower() in banned_users:
	print("Banned User")
else:
	print("Welcome")

#Test 5
banned_users = ["emily","susan","rebecca"]
user = "marie"

print("Is 'marie' allowed to post. I suspect she is.")
if user not in banned_users:
	print(f"{user.title()}, my dear, you can post a response if you wish.")




#From 0501_conditional_tests.py