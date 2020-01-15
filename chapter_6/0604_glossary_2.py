#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 6

#An update om the glossary providing simple definitions

glossary = {
	'for_loop' : ' A control flow statement for specifying iteration' ,
	'list' : ' The list is a collection of ordered and changeable elements' ,
	'comprehension' : 'Comprehensions in Python provide us with a short and concise way to construct new sequences ' ,
	'title()' : 'The title() method is used to convert the first character in each word to Uppercase and the remaining to lower' ,
	'lower()' : 'The lower() method returns the lowercased string from the given string. It converts all uppercase characters to lowercase' ,

	}

	#Print the key and the definiton using a loop.

for key, value in sorted(glossary.items()):
	print(f'{key.title()}{value}')