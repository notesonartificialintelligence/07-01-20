#Gabriel Abraham
#notesinartificialintelligence
#Python Crash Course - Chapter 8

def make_shirt(shirt_size, shirt_message):
	"""Print shirt size and message"""
	print(f"The message '{shirt_message.title()}', will be printed on a {shirt_size.title()} tshirt")

#Call the function once using positional arguments, and then using the keyword argument.

make_shirt('m', 'hello earthlings')

make_shirt(shirt_message = "I'm from out of space", shirt_size = 'l')