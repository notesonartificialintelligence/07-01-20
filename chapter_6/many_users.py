#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 6

#A dicionary in a dictionary

users = {
		'aeinstein' : {
			'first' : 'albert',
			'last' : 'einstein',
			'location' : 'princeston',
			},

		'mcurie' : {
			'first' : 'marie',
			'last' : 'curie',
			'location' : 'paris',
			},
	}


for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = f"{user_info['location']}"

	print(f"\tFull name: {full_name.title()}")
	print(f'\tlocation: {location.title()}')