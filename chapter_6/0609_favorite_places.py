#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 6


#New Dictionary 
favorite_places = {
	'James' : ['London','Paris','New York'],
	'Samantha' : ['Mexico','Bali','Manchester'],
	'Diana' : ['London','Paris','Bali'],
	'tim' : ['London']
	}

#Loop through the ditionary, if the length of the list is greater than 1, print out all of the elements
for key, values in favorite_places.items():
	if len(values) > 1:
		print(f"\n{key.title()}'s favorite places are: ")

		for value in values:
			print("\t" + value.title()) 
	else:
		print(f"\n{key.title()}'s favorite place is: {value.title()}")
		#This line prints out Bali, now, I'm not too sure why. I've had a full day at university, and it's late in the evening.
		#So it's an issue that can be solved for another day.