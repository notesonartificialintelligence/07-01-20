#Gabriel Abraham
#notesonartificialintelligence
#Create a list of the numbers one to 1M, and then use a for loop to print the numbers.

#List Comprehension
#1, Begin with a descriptive name for the list
#2, Define the expression for the values you want to store in the new list. value**2
#3, Write the for loop to generate the numbers you want to feed into the expression.


million_list = print([value for value in range(1,1_000_001)])

#If you run it and it takes to long press "CTRL + C" to stop.

million_list_2 = [value for value in range(1,1_000_001,10)]

print(million_list_2)