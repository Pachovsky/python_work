def make_album(artist, album, numbers=""):
    """Return a dictionary of artist with their albums."""
    albums = {
        "Artist": artist.title(), 
        "Album": album.title()
        }
    if numbers:
        albums["Numbers"] = numbers
    return albums

artist_prompt = "\nPlease tell me your favorite artist: "
album_prompt = "Tell me their best album: "

print("Enter 'quit' to quit.")

while True:
    artist = input(artist_prompt)
    if artist == "quit":
        break

    album = input(album_prompt)
    if album == "quit":
        break

    made_album = make_album(artist, album)

    print(made_album)

print("\nThanks for responding!")