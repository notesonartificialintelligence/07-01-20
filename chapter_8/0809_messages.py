#Gabriel Abraham
#notesofartificialintelligence
#Python Crash Course - Chapter 8

def show_messages(message_list):
	"""Print elements from a list"""
	for message in message_list:
		print(message)

messages = ['Mental peace and Clarity', 'Abundance and Love', 'Radient energy and God form']

#I'll pass it a cpoy and not the original list.
show_messages(messages[:])
