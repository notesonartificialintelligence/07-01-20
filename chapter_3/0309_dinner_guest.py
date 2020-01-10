#Gabriel Abraham
#notesonartificialintelligence
# Working with an eariler program, use the len() funciton to show the amount or people invited to dinenr.
names = ['andrew','john','steve']

names.insert(0, 'margret')
names.insert(2, 'tim')
names.append('woz')

message = ", would you care to join us for dinner this saturday?"


print(f"{names[0].title()}{message}")
print(f"{names[1].title()}{message}")
print(f"{names[2].title()}{message}")
print(f"{names[3].title()}{message}")
print(f"{names[4].title()}{message}")
print(f"{names[-1].title()}{message}")

print(f"Mother invited {len(names)} people to dinner on saturday.")