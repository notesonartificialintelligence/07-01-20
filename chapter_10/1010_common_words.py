#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 10

#Visit project Gutenbery and find a few texts you'd like to analyse.
#Download the file, then use the count methed to find out how many times a word or phrase
#appears in a string.
#The word will be 'the'

fileName ='pride_and_prejudice.txt'

with open(fileName) as file_object:
	contents = file_object.read()

total_amount = contents.lower().count("the")

total_amount_the = contents.lower().count("the ")

print(f"The characters 'the' appears in that particular sequence {total_amount} times in the text.\n")
print(f"The word ' the ' appears {total_amount_the} times in the text.\n")
