#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 7

#Use the list from the previous exercise, ensure 'Pastrami' appears 3 times.
sandwich_orders = ['Pastrami', 'Cheese and Onion', 'Pastrami', 'Veganlight', 'Pastrami','Meat Feast', 'Fast Tuna']

print("The Deli has ran out of Pastrami")

#Use a while loop to remove all occurrences of Pastrami
while 'Pastrami' in sandwich_orders:
	sandwich_orders.remove('Pastrami')

finshed_sandwiches = []

#While the sandwich list is not empty
while sandwich_orders:
	#Pop the last element from the list. Store it as completed_orders
	completed_orders = sandwich_orders.pop()

	print(f"The {completed_orders} sandwich has been made. ")
	#Append the completed_order onto the new empty list.
	finshed_sandwiches.append(completed_orders)

	print("The following sanwiches have been made: ")
#Loop through the items in the list, and print it out.
for value in finshed_sandwiches:

	print("\t" + value.title())
