#Gabriel Abraham
#notesonartificialintelligence
#Improve prior written code.

dimensions = (200, 50)


#Writing over a Tuple: Assigning  new value to a variable that represents a tuple.
print("Original Dimensions:")
for dimension in dimensions:
	print(dimension)


dimensions = (400,100)
print("\n Modified dimensions:")
for dimension in dimensions:
	print(dimension)


#Create a Tuple of items and then print the items.
meals = ("Avocado","Banana", "Huel", "Nuts", "Chickpeas")

for meal in meals:
	print(meal)

#Create a list, and then slice that list.
my_foods = ["pizza","falafel","carrot cake"]
friends_foods = my_foods[:]

#Then print the two lists using a for loop.
for food in my_foods:
	print(food.title())
print("These are my foods \n")

for friends_food in friends_foods:
	print(friends_food.title())