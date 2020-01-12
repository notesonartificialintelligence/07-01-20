#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 5

#This program will loop through the list checking for 'bmw', 
#which, when found will be printed in upper case.

cars = ["audi","bmw","subaru","toyota"]

for car in cars:
	if car == "bwm":
		print(car.upper())
	else:
		print(car.title())