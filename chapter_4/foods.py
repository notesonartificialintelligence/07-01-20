#Gabriel Abraham
#notesonartificialintelligence
#copying a list

my_foods = ["pizza","falafel","carrot cake"]
friends_foods = my_foods[:]

#To copy a list we make a slice of the full list, this is done by omitting the first adn second index.

print("My favorite foods are:")
print(my_foods)

print("\n My friends favorite foods are:")
print(friends_foods)

#To show that we have indeed created two seperate list, we'll append a new value to friends_foods

my_foods.append("cannoli")
friends_foods.append("ice cream")


print("\nMy favorite foods are:")
print(my_foods)

print("\n My friends favorite foods are:")
print(friends_foods)