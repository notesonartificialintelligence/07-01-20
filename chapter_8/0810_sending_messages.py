#Gabriel Abraham
#notesofartificialintelligence
#Python Crash Course - Chapter 8

#Start with a copy of the previous message. Modify it so that it moves
#each message to a new list.

def show_messages(message_list, sent_messages):
	"""Print elements from a list, and then move to another list"""

	sent_message = []
	while message_list:
		print(message_list)
		completed_messages = message_list.pop()

		sent_message.append(completed_messages)

	print_message(new_list = sent_message, old_list = message_list)

#The print out both list.
def print_message(old_list, new_list):
	print(f"Here is the old list: {old_list}")
	print(f"Here is the new, updated list: {new_list}")


messages = ['Mental peace and Clarity', 'Abundance and Love', 'Radient energy and God form']
empty_list = []

#I'll pass it a cpoy and not the original list.
show_messages(messages[:], empty_list)
