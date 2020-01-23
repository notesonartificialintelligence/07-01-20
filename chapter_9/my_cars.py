#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 9

#Importing multiple classes from a module
from car import Car
from electric_car import ElectricCar as EC

my_beetle = Car('volkswagen', 'beetle', 2020)
print(my_beetle.get_descriptive_name())

my_tesla = EC('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())
