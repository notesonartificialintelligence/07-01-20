#Gabriel Abraham
#notesonartificialintelligence

names = ['andrew','john','steve']

message = ", your presence is requested downstairs."


unavailable_guest = names.pop()

print(f"{names[0].title()}{message}")
print(f"{names[1].title()}{message}")

#Call the program stating the guest who will not be able ot make it
print(f"Unfortunately,{unavailable_guest.title()} will not be able to attend.")

#Replace the name of the guest who will not be attending.
# I'll changing it slightly, I'll replace John with margret, and then add another guest.

names[1] = 'mergret'
names.append('Tim')

#Print out the contents of the list
print(names)