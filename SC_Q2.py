def load_data():
    global songs_db
    filename = input("Enter the file name to load songs: ")
    try:
      with open(filename, "r") as file:
        songs_db.clear()
        for line in file:
            parts = line.strip().split('","')
            if len(parts) == 5:
                title = parts[0].replace('"', '')                    artist = parts[1]
                    album = parts[2]
                    genre = parts[3]
                    duration = parts[4].replace('"', '')
                    song = {
                       "Title": title,
                       "Album": album,
                       "Genre": genre,
                       "Duration": duration
                    }
                    if artist not in songs_db:
                       songs_db[artist] = []
                    songs_db[artist].append(song)   
      print(f"Songs loaded from {filename}.")
    except FileNotFoundError:
      print("Error: File not found.") 

def main():
    while True:
      print("\nDeveloper Menu:")
      print("1. Load Song Data")
      print("2. View Songs Database")
      print("3. Delete a Song")
      print("4. Modify a Song")
      print("5. Exit")
      choice = input("Select an option: ")
            if choice == "1":
               load_data()
            elif choice == "2":
                view_database()  
            elif choice == "3":
                delete_song()
            elif choice == "4":
                modify_song()
            elif choice == "5":
                print("Exiting the application. Goodbye!")
                break         
            else:
                print("Invalid option. Please try again.")
            
def view_database():
    if not songs_db:
      print("No songs loaded.")
      return
    print("Songs Database:")
    print("Title                          Artist                       Genre")
    print("=" * 70)
    for artist in songs_db:
      for song in songs_db[artist]:
        print(f'"{song["Title"]}"'.ljust(30), f'"{artist}"'.ljust(30), f'"{song["Genre"]}"')


def delete_song():
    artist = input('Enter the artist\'s name of the song to delete: ')
    title = input('Enter the title of the song to delete: ')
    if artist in songs_db:
      for song in songs_db[artist]:
        if song["Title"] == title:
          songs_db[artist].remove(song)
          if not songs_db[artist]:
            del songs_db[artist]
          print(f'Deleted "{title}" by "{artist}" from the database.')
          return
    print("Song not found.")


def modify_song():
    artist = input('Enter the artist\'s name of the song to modify: ')
    title = input('Enter the title of the song to modify: ')
    if artist in songs_db:
      for song in songs_db[artist]:
        if song["Title"] == title:
          print(f'Current details: Title: "{title}", Album: "{song["Album"]}", Genre: "{song["Genre"]}", Duration: "{song["Duration"]}"')
          new_album = input("Enter new album (or press Enter to keep current): ")
          new_genre = input("Enter new genre (or press Enter to keep current): ")
          new_duration = input("Enter new duration (or press Enter to keep current): ")
          if new_album:
            song["Album"] = new_album
          if new_genre:
            song["Genre"] = new_genre
          if new_duration:
            song["Duration"] = new_duration    
          print(f'Modified "{title}" by "{artist}".')
          return
    print("Song not found.")


songs_db = {}

if __name__ == "__main__":
    main()