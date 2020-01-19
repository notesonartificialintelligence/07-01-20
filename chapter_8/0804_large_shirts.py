#Gabriel Abraham
#notesinartificialintelligence
#Python Crash Course - Chapter 8

#Modify the previous exmple so that the shirts have a default message and size

def make_shirt(shirt_size = "l", shirt_message = "I love python"):
	"""Print shirt size and message: with default parameters."""
	print(f"The message '{shirt_message.title()}', will be printed on a {shirt_size.title()} tshirt")

#Call the function once using positional arguments, and then using the keyword argument.

make_shirt('m', 'hello earthlings')

make_shirt(shirt_message = "I'm from out of space", shirt_size = 'l')
make_shirt()