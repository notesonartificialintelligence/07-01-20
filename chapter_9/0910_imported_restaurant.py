#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 9

#Using our latest Restaurant class, store it in a module.
#Make a seperate file that imports Restaurant...then call a method to ensure that it workd properly

#Import the restaurant class from the file appropiately named, using a type alias.
from restaurant import Restaurant as RS

new_restaurant = RS('ranaaghor', 'indian')

new_restaurant.describe_restaurant()