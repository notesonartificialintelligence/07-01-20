#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 6

#A Simple Dictionary

alien_0 = {'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])

#Assume a person is playing a game, and they've just shot down an alien.

new_points = alien_0['points']
print(f"You've just earned {new_points} points!")

#Adding new key value pairs to the dictionary.

alien_0['x_position'] = 0
alien_0['y_position'] = 25


#Starting with an empty dictionary.

alien_1 = {}

alien_1['color'] = 'green'
alien_1['points'] = 5

#Modifying the values in a Dictionary.


print(f"The alien is {alien_1['color']}")

alien_1['color'] = 'yellow'

print(f"The alien is {alien_1['color']}")
print(f"The alien is {alien_1['color']}")

#A more interesting example.
alien_2 = {'x_position' : 0,'y_position' : 25,'speed':'medium'}
print(f"Original position: {alien_2['x_position']}")

 #Move the alien to the right.
 #Determine how far to move the alien based on it's current speed.

if alien_2['speed'] == 'slow':
 	x_increment = 1
elif alien_2['speed'] == 'medium':
 	x_increment = 2
else:
 	#This must be a fast alien
 	 x_increment = 3

#The new position is the old position plus the increment.
alien_2['x_position'] = alien_2['x_position'] + x_increment

print(f"New position: {alien_2['x_position']}")

#Removing key value pairs
del alien_0['points']
print(alien_0)

