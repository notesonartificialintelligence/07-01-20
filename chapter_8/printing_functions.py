#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 8
#Module

def print_models(unprinted_designs, completed_models):
	"""
	Simulate printing each deisn, until none are left.
	Move each design to completed_models after pringing.
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()

		print(f"Printing model: {current_design}")
		completed_models.append(current_design)


def show_completed_models(completed_models):
	"""show all the models that were printed."""
	print("\nThe following models have been printed: ")
	for completed_model in completed_models:
		print(completed_model)