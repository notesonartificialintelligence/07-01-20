#Gabriel Abraham
#notesonartificialintelligence
#Slicing a List


players = ["charles","martina","michael","florence","eli"]

#Print the first three elements of the list
print(players[0:3])

#Omiting the first element.
players[1:4]
#"martina","michael","florence" will be printed 

# Just omiting the first index. The full list will still be printed.
players[:4]
#"charles","martina","michael","florence" will be printed

#The full list from the 2nd list element.(3)
players[2:]
#"michael","florence","eli" Will be printed

#The last 3 elements of the list
players[-3:]
#"michael","florence","eli" will be printed.

#Looping though only a poriton of the list

print("Here are the first three players on my team:")
for player in players[0:3]:
	print(player.title())
