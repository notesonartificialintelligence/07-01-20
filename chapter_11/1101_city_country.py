#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 11

#Write a function that accepts two parameters: a city name and a country name.
#The function should return a single string of the form
#city, country. Then test.

def city_country(city, country):
	"""output the city and country."""
	output = f"{city}, {country}"

	return output.title()
