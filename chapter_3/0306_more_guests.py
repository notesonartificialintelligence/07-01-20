#Gabriel Abraham
#notesonartificialintelligence

names = ['andrew','john','steve']

message = ", would you care to join us for dinner this saturday?"

print(f"The invitations will be deilvered to: {names[0].title()},{names[1].title()} and {names[2].title()}")


print("look, there's a larger table.")

names.insert(0, 'margret')
names.insert(2, 'tim')
names.append('woz')


print(f"{names[0].title()}{message}")
print(f"{names[1].title()}{message}")
print(f"{names[2].title()}{message}")
print(f"{names[3].title()}{message}")
print(f"{names[4].title()}{message}")
print(f"{names[-1].title()}{message}")