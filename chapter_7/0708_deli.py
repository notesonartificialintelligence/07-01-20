#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 7

#Make a list called sandwich_orders, and fill it with the names of various sandwiches.
#Then make an empty list called finshed_sandwiches...

sandwich_orders = ['Cheese and Onion', 'Veganlight', 'Meat Feast', 'Fast Tuna']

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
