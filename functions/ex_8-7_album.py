# make a function called make_album() that builds a dictionary describing a music album
# fuction should take: an artist name and an album title
# function should return a dictionary containg this information
# use the function to make three dictionaries representing different albums
# use None to add an optional parameter to make_album that stores the number of songs on an album
# if the calling line includes a value of nbr songs, add that value to the album's dictionary
# make at least one function call that includes the number of album songs

def make_album(artist_name, album_title, songs='None'):
    album = {'name':artist_name, 'title':album_title}
    if songs:
        album['songs'] = songs
    return album
artist = make_album('katie melua', 'ultimate collection')
print(artist) 
artist = make_album("eniah", "grand", 7)
print(artist)
artist = make_album("bailey rushlow", "covers with friends", 17)
print(artist)
