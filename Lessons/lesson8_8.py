def make_album(artist, title, songs=None):
	album = {'artist' : artist, 'title' : title}
	if songs:
		album['songs'] = songs
	return album


while True:
	print('Please enter artist name and album title')
	print('For quit enter \'q\'')
	artist = input('Artist name:')
	title = input('Album title:')
	songs =input('Songs cout (or just press Entrer): ')
	album = make_album(artist, title, songs)
	if 'q' in album.values():
		break
	message = f"The album '{album['title'].title()}' of artist {album['artist'].title()}."
	if 'songs' in album:
		message += f" Consist of  {album['songs']} songs"
	print(message)