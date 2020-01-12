#Gabriel Abraham
#notesonartificialintelligence
#Make a copy of the "pizza list", and then do the following:

minerals = ["Selenium", "Calcium","Magnesium"]
#Creating a copy of minerals list.
friend_minerals = minerals[:]

#Add a different pizza to the friend_mineral
friend_minerals.append("Cobalt")

#Prove that the lists have are indeed to separate lists
print("My favorite minerals are: ")

for mineral in minerals:
	print(mineral)


#Then use another foor loop to print the other list.
print("My friends favorite minerals are: ")

for friend_mineral in friend_minerals:
	print(friend_mineral)
