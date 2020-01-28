#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 11

#Modify the city country function so that it requires a third parameter population.

#Write a function that accepts two parameters: a city name and a country name.
#The function should return a single string of the form
#city, country. Then test.

def city_country(city, country, population):
	"""output the city and country."""
	output = f"{city}, {country} - population {population}"

	return output.title()
