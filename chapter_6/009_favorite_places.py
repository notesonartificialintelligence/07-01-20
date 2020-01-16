#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 6


#New Dictionary favorite places
favorite_places = {
	'James' : ['London','Paris','New York'],
	'Samantha' : ['Mexico','Bali','Manchester'],
	'Diana' : ['London','Paris','Bali'],
	'tim' : ['London']
	}


for key, values in favorite_places.items():
	if len(values) > 1:
		print(f"\n{key.title()}'s favorite places are: ")

		for value in values:
			print("\t" + value.title()) 
	else:
		print(f"\n{key.title()}'s favorite place is: {value.title()}")