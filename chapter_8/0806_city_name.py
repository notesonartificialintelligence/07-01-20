#Gabriel Abraham
#notesinartificialintelligence
#Python Crash Course - Chapter 8

def city_country(city, country):

	location = f"{city.title()}, {country.title()}"

	return(location)

location = city_country('santiago','chile')
print(location)

location = city_country('london','great britian')
print(location)

location = city_country('manchester','great britian')
print(location)