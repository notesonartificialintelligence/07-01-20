#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 6

#Make a dictionary called cities, use the names of three cities as keys in the dictionary
#Create a dictionary of information about each city and include the city the country is in.
#A dictionary in a dictionary.


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