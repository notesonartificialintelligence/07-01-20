#Gabriel Abraham
#notesonartificialintelligence
#Use a for loop to print out the elements in the list

my_foods = ["pizza","falafel","carrot cake"]
friends_foods = my_foods[:]

for food in my_foods:
	print(food.title())
print("These are my foods \n")

for friends_food in friends_foods:
	print(friends_food.title())