#Gabriel Abraham
#notesofartificialintelligence
#Python Crash Course - Chapter 8

def create_sandwiches(*fillings):
	"""Print a summary of the sandwiches being ordered."""
	print(f"This sandwich will be filled with: \n")
	for filling in fillings:
		print(filling.title())


create_sandwiches('Green','Wood','Rose','oud')
create_sandwiches('Ham', 'butter', 'cheese')
create_sandwiches('spinach', 'cress', 'vegan free butter', 'avocados')