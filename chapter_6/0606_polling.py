#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 6

#Creating a list of people who should take a favorite languages poll
names = ['jen','tim','sarah', 'edward', 'phil', 'james']

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}


#Loop though the list, if the person is question has taken the poll, thank them ,if not ask them to do so.
#At first i had created a nested loop, looping through both the dicitonary and the list.

for name in names:
		if name in favorite_languages.keys():
			print(f"Thank you, {name.title()}\n.")
		else:
			print(f"{name.title()}, you've been invited to complete the poll.\n")

