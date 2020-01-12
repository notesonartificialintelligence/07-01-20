#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 5

#Write a series of conditional tests. Print a statement describing each test.

#Test 1
car = "subaru"
print("Is car == 'subaru'? I predict true.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == "audi")

#Test 2
age = 12
print("Is age >'10'? I predict true.")
print(age > 10)

print("\nIs age <'10'? I predict False.")
print(age <10)

#Test 3
user = "tim"
banned_users = ["andrew","carolina","david"]

print("Is 'Tim' banned? I predict false.\n")

if user in banned_users:
	print("Banned User")
else:
	print("Welcome")


#Test 4
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




