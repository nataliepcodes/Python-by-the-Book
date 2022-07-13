# start with program from ex 8-7
# write a while loop asking user's to enter an album's artist and title
# call make_album function with the user's input and print a dictionary
# be sure to quit value in the while loop

def make_album(artist_name, album_title):
    album = {'name':artist_name, 'title':album_title}
    return album


while True:
    print("\nTo search for an album, please enter the artist's name and the album title.")
    print(">> To stop the program, enter 'quit' <<\n")

    artist_name = input("artist's name: ")
    if artist_name == 'quit':
        break

    album_title = input("album title: ")
    if album_title == 'quit':
        break;

    user_album = make_album(artist_name, album_title)

    print(user_album)
    