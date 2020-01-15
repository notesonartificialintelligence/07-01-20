#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 6

favorite_languages = {
	'jen': ['python' , 'ruby'],
	'sarah': 'c',
	'edward': ['ruby' , 'go'],
	'phil': ['python', 'haskell'],
	}

#Looping through all the keys and values in the dicionary.
#The items() function will return a list of key-value pairs

for name, languages in favorite_languages.items():
	if len(languages) > 1:
		print(f"\n{name.title()}'s favorite languages are: ")

		#We hold the variable languages becuase we know that the value will be a list, We then iterate through the list.
		for language in languages:
			print("\t" + language.title())

	else:
		print(f"\n{name.title()}'s favorite language is: {languages.title()} ")

