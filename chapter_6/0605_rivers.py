#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 6

#make a dictionary that contains three rivers, also mention the city the river runs in.


rivers = {
		'nile' : 'egypt',
		'gange' : 'india',
		'thames' : 'london',
	}

	#Create three loops which: print the key and value pait, the value and the key.


for key, value in sorted(rivers.items()):
	if value == 'london':
		print(f"The river {key.title()} runs thorugh the city of {value.title()}")
	else:
		print(f"The river {key.title()} runs through the country of {value.title()}")
print('\n')


for value in sorted(rivers.values()):
	if value == 'london':
		print(f"The city of {value.title()} has a river.")
	else:
		print(f"The country of {value.title()} has a river")
print('\n')

for key in sorted(rivers.keys()):
	print(f"{key.title()}, is the name of a river.")

print('\n')