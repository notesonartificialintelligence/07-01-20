#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 10

filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.rstrip()


#Is your birthday contained in Pi?
#You'll need to have a test file containing the first 1_000_000 decimal places of pi.

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi.")
print(pi_string)
print(len(pi_string))