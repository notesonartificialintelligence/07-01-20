#Gabriel Abraham
#notesinartificialintelligence
#Python Crash Course - Chapter 8

def describe_city(city, country = "Great Britian"):
	"""Print the city and country"""
	print(f"{city.title()} is in {country.title()}")

describe_city('london')
describe_city('manchester')
describe_city('mezico city', 'mexico')