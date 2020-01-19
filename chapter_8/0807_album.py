#Gabriel Abraham
#notesinartificialintelligence
#Python Crash Course - Chapter 8

def make_album(artist_name, album_title, number_of_songs = ''):
	"""Music Album Dictionary"""

	music_album = {'Name' : artist_name, 'Album Name' : album_title}

	if number_of_songs:
		music_album['Number Of Songs'] = number_of_songs

	return (music_album)

album = make_album('Pink Floyd', 'Dark Side of the Moon')
print(album)

album = make_album('The Beatles', "Sgt. Pepper's Lonely Hearts Club Band", "16")
print(album)

album = make_album('The Beatles', 'Abbey Road')
print(album)