#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 8

from pizza import make_pizza as mp

#Using an alias, this is used if the function we're importing might conflict with 
#an existing name in our program, or it's long.
#In using a alias on an imported function, we will not have to use the dot operator.


mp(16, 'pepperoni')
mp(12, 'mushrooms','green peppers','extra cheese')