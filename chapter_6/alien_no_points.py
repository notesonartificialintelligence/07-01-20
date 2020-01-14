#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 6

#Asking for a value key that does not exist.
alien_0 = {'color':'green','speed':'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)


#If the key exists that value will be printed out, if it does not that string that follows will be printed.
