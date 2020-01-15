#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 6


#Create three dictionaries, store them in a list. Print out everything you know about each
person_1 = {
		'first_name': 'James',
		'last_name': 'molton',
		'age': 32,
		'city': 'london',	
	}

person_2 = {
		'first_name': 'Tim',
		'last_name': 'Clark',
		'age': 55,
		'city': 'Edinburgh',	
	}
person_3 = {
		'first_name': 'Samantha',
		'last_name': 'Sweeney',
		'age': 66,
		'city': 'Manchester',	
	}		

people_list = [person_1, person_2, person_3]


#Now, this program has taken me over 20 minutes to figure out.

#Iterate through the elements in the list.
for people in people_list:

	#Once we have the name of the dictionary, use the key to load the value
	full_name = f"{people['first_name']} {people['last_name']}"
	age = f"{people['age']}"
	city = f"{people['city']}"

	print(f"The details of the users are as follows:")
	print(f"Full name : {full_name}")
	print(f"Age : {age}")
	print(f"City : {city}\n")
	