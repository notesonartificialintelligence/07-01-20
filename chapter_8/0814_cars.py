#Gabriel Abraham
#notesofartificialintelligence
#Python Crash Course - Chapter 8

def create_car(car_make, car_type, **car_info):
	"""Build a dictionary containing everything we know about cars"""

	car_info['car_make'] = car_make
	car_info['car_type'] = car_type

	print(car_info)


create_car('ford', 'pickup', color = 'blue', tow_package = True)