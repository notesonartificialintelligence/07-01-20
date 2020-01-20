#Gabriel Abraham
#notesofartificialintelligence
#Python Crash Course - Chapter 8


#** allows the user to pass in Arbitrary Keyword Arguments.
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['First_name'] = first
	user_info['last_name'] = last

	return user_info

user_profile = build_profile('Gabriel', 'Abraham', location = 'Edinburgh', field = 'Artificial Intelligence')


print(user_profile)