#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 9

#Import the electricCar class from the file car
from electric_car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', '2019')

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()