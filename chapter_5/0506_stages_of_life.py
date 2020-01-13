#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 5

#Write an if statement that determines a person's stage at life. Set a value for the variable age, and then:

age = 46

if age < 2:
	print("The person in question is a baby.")
elif age < 4:
	print("the person is question is a toddler")
elif age < 13:
	print("The person in question is still a child")
elif age < 20:
	print("The person in quesiton is a teenager.")
elif age < 65:
	print("The person in question if an adult.")
else:
	print("The person in question is an elder.")