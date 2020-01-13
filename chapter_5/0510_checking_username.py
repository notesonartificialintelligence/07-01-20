#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 5

#Create a program to ensure that every username is unique.


current_users = ["je123","tony54","artimis","admin","stones"]

new_users = ["James","Tony","artimis","Bradley","stones"]

for new_user in new_users:
	for current_user in current_users:
		if new_user.lower() == current_user.lower():
			print("That username is already is use. ")
		else:
			print("That username is available.")
			#An extra check I've added.
			print(f"{new_user} was checked against {current_user}")