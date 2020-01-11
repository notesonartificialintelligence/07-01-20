#Gabriel Abraham
#notesonartificialintelligence
#A simple porgram printing out the square numbers of the values 1 - 10


#squared_list = []

#square_numbers = range(1,11)

#for square_number in square_numbers:
#	squared = square_number ** 2
#	squared_list.append(squared)

#print(squared_list)

										#The above program done concisely 

#squared_list = []

#for value in range(1,11):
#	squared_list.append(value ** 2)

#print(squared_list)

										#The above program done with list comprehensions


squared_list = [value ** 2 for value in range(1,11)]

print(squared_list)

#1, Begin with a descriptive name for the list
#2, Define the expression for the values you want to store in the new list. value**2
#3, Write the for loop to generate the numbers you want to feed into the expression.


#List comprehensions will be used when I create the later tasks.