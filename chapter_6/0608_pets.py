#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 6

#Make several dictionaries where each dictionary represents a different pet.
#Include the kind of animal and the owners name, store in a list, then loop thorugh the list
#Then print everything.


pet_1 = {
    'name' : 'kandy',
    'animal' : 'dog',
    'owners' : 'Gabriel',
    }

pet_2 = {
    'name' : 'tilly',
    'animal' : 'cat',
    'owners' : 'Deborah',
    }

pet_3 = {
    'name' : 'philly',
    'animal' : 'horse',
    'owners' : 'James',
    }

pet_4 = {
    'name' : 'sash',
    'animal' : 'dog',
    'owners' : 'Michael',
    }

pet_5 = {
    'name' : 'coco',
    'animal' : 'cat',
    'owners' : 'Anais',
    }

pet_6 = {
    'name' : 'speed',
    'animal' : 'horse',
    'owners' : 'Samantha',
    }

pet_7 = {
    'name' : 'apple',
    'animal' : 'horse',
    'owners' : 'George',
    }

pets = [pet_1, pet_2, pet_3, pet_4, pet_5, pet_6, pet_7]


for pet in pets:
    print(f"Details about the pet are as follows:\n")
    print(f"Name: { pet['name']}")
    print(f"Animal: {pet['animal']}")
    print(f"Owners: {pet['owners']}")