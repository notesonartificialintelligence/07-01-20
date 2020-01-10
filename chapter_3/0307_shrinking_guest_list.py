#Gabriel Abraham
#notesonartificialintelligence

names = ['andrew','john','steve']

message = ", would you care to join us for dinner this saturday?"

names.insert(0, 'margret')
names.insert(2, 'tim')
names.append('woz')


print(f"The invitations will be deilvered to: {names[0].title()},{names[1].title()} and {names[2].title()}")
print(f"The invitations will be deilvered to: {names[3].title()},{names[4].title()} and {names[-1].title()}")


print(f"{names[0].title()}{message}")
print(f"{names[1].title()}{message}")
print(f"{names[2].title()}{message}")
print(f"{names[3].title()}{message}")
print(f"{names[4].title()}{message}")
print(f"{names[-1].title()}{message}")

print("look, there's a larger table, but the issue is that were only able to invite two people.")

#Use pop to remove guest from the list one by one, until two remain,
uninvited_guest = names.pop()
print(f"Apologies, {uninvited_guest}, we've just out that there's not enough space in the garden.")
uninvited_guest = names.pop()
print(f"Apologies, {uninvited_guest}, we've just out that there's not enough space in the garden.")
uninvited_guest = names.pop()
print(f"Apologies, {uninvited_guest}, we've just out that there's not enough space in the garden.")
uninvited_guest = names.pop()
print(f"Apologies, {uninvited_guest}, we've just out that there's not enough space in the garden.")

#Print a message to the remaining guests.ß
new_message = ", we look forward to seeing you on saturday."
print(f"{names[0].title()}{new_message}")
print(f"{names[1].title()}{new_message}")

#Delete the entries in the list
del names[0]
del names[0]

#print the empty list
print(names)


