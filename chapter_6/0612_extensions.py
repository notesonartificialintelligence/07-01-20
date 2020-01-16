#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 6

#I've just added the program from the other lesson, the reason are as follows:
	#Over last 6 exercises, I had been confused with list and dictionaries. 
	#This was because of the struccture of the book, and also using list in dictionaries, lists in lists, dictionaries in list.
	#Gosh, thankfully I understand it all. I've also had a really long day at university , lectures followed by group meetings. 
	#followed by everything else. 
cities = {
    'London' : {'Country' : 'United Kingdom',
                'Population' : '8.9 Million',
                'fact' : 'People who come from london are called Londoners',
                },
    'Bali' : {'Country' : 'Indonesia',
                'Population' : '4.3 Million',
                'fact' : 'Independence Day is celebrated on August 17',
                },
    'Mexico City' : {'Country' : 'Mexico',
                'Population' : '21.3 Million',
                'fact' : 'Mexico City is the largest metropolitan area of the Western Hemisphere,',
                }
    }


for city, values in cities.items():
    print(f"Information about {city} are as follows:\n")
    for key, value in values.items():
        print(f"{key.title()}, {value}")