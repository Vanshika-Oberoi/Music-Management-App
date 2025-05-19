def load_datbase():
  songs = {}
  try:
    with open("songs_database.txt","r",encoding="utf-8")as file:
      for line in file:
        parts=line.strip().split(",")
        if len(parts)==5:
          title=parts[0].replace('"','').strip()
          artist=parts[1].replace('"','').strip()
          album=parts[2].replace('"','').strip()
          genre=parts[3].replace('"','').strip()
          duration=parts[4].replace('"','').strip()
          songs[title.lower()]={
            "title":title,
            "artist":artist,
            "album":album,
            "genre":genre,
            "duration":duration
          }
    return songs

  except FileNotFoundError:
      print("Error: 'songs_database.txt' not found.")
      return {}

def search_by_title(database, title):
  print(f"Searching for songs with title: '{title}'")
  song = database.get(title.lower())
  if song:
    print(f"Found: '{song['title']}' by {song['artist']} (Album: {song['album']}, Genre: {song['genre']}, Duration: {song['duration']})")
  else:
    print(f"Song title '{title}' does not exist in the database.")        

def search_by_artist(database,artist):
  print(f"Searching for songs by artist: '{artist}'")
  found = False
  for song in database.values():
    if song['artist'].lower() == artist.lower():
      print(f"Found: '{song['title']}' (Album: {song['album']}, Genre: {song['genre']}, Duration: {song['duration']})")
      found=True
  if not found:
    print(f"No songs found for artist '{artist}'.")    

def main():
  database=load_datbase()
  while True:
    print("--- User Menu ---")
    print("1. Search for a Song by Title")
    print("2. Search for All Songs by an Artist")
    print("3. Exit")
    choice = input("Select an option: ")
    if choice == "1":
      title = input("Enter the song title to search: ")
      search_by_title(database, title)
    elif choice == "2":
      artist = input("Enter the artist's name to search: ")
      search_by_artist(database, artist)
    elif choice == "3":
      print("Exiting the Songs Management System. Goodbye!")
      break
    else:
      continue


if __name__ == "__main__":
    main()            

