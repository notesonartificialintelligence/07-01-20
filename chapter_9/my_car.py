#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 9

#Import the Car class from the file car.
from car import Car

#Create a new instance of this car.
my_new_car = Car('audi','a4',2020)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()