#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 7


#In using prompts ensure to include one that tells the user what they should enter
#If the prompt is going to be over 2 lines, do the following.

prompt = "If you tell use who you are, we can personalise the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(name)
