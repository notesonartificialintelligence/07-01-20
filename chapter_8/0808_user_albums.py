#Gabriel Abraham
#notesinartificialintelligence
#Python Crash Course - Chapter 8

def make_album(artist_name, album_title, number_of_songs = ''):
	"""Music Album Dictionary"""

	music_album = {'Name' : artist_name, 'Album Name' : album_title}

	if number_of_songs:
		music_album['Number Of Songs'] = number_of_songs

	return (music_album)

while True:

	print("Welcome, this is a Music Album catalog.")
	print("(enter 'q' to quit)")

	artist_name = input("Enter the artist name:\n")

	if artist_name == 'q':
		print('Goodbye')
		break

	album_name = input("Enter the album name:\n")
	if album_name == 'q':
		print('Goodbye')
		break

	album = make_album(artist_name, album_name)
	print(f"Entry {album}, has been added")
