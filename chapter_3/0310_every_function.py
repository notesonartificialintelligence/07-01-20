#Gabriel Abraham
#notesonartificialintelligence
#Write a program that used the functions introduced in this chapter at least once.


function_list = ["mountains","rivers","countries","cities","languages"]
print(function_list)

del function_list[0]

print(f"This is now the current list: {function_list}")

function_list.append("transportation")

function_list.insert(3, "shops")

function_list.sort()

print(f"This is the current list printed out in alphabetical order: {function_list}")

function_list.reverse()
print(f"This is the list reversed: {function_list}")

print(f"The current length of the list is: {len(function_list)}")
print(function_list)
print("Mind you, the list has been permantly reversed")


poped_item = function_list.pop()

print(f"{poped_item.title()}, has been poped from the list.")

function_list.remove("rivers")
print(function_list)

function_list.insert(4,"activities")

print(function_list)