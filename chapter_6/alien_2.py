#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 6


#A set of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

#A list with dictionary elements
alienss = [alien_0, alien_1, alien_2]

for alien1 in alienss:
	print(alien1)

print(f'\n')



#Make an empty list for storing aliens

aliens = []

for alien_number in range(30):
	new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
	aliens.append(new_alien)


for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10


#Show the first 5 aliens.
for alien in aliens[:5]:
	print(alien)
print('...')


#Show how many aliens have been creaated.
print(f'Total number of aliens: {len(aliens)}')