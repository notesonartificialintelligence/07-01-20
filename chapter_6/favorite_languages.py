#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 6

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

#Looping through all the keys and values in the dicionary.
#The items() function will return a list of key-value pairs

for name, language in favorite_languages.items():
	print(f"{name.title()} favorite language is {language.title()}")


#Only looping through the keys of the dictionary
#Understand that you do not have to add the key function.

for name in favorite_languages.keys():
	print(name.title())
