#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 5

#Make a list of your favorite fruits, and then write a series of 
#independent if statements that check for cetain fruits in your list.


favorite_fruits = ["apple", "banana", "pear", "strawberry", "blueberry"]

if 'apple' in favorite_fruits:
	print("You really like apples!")

if 'banana' in favorite_fruits:
	print("You really like bananas!")

if 'pear' in favorite_fruits:
	print("You really like pears!")

if 'strawberry' in favorite_fruits:
	print("You really like strawbrries!")

if 'blueberry' in favorite_fruits:
	print("You really like bluebrrries!")

#A much fast way to do this.

for fruits in favorite_fruits:
	print(f"You really enjoy eating an {fruits.title()}")

#Just a random list comprehension to ensure I remember it.
#The power of certain value between 1 and 9, whilst increasing the increment by 2
list_comp = [value ** 2 for value in range(1,10,2)]

print(list_comp)
