class Playlist:

    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []
        print(f"Playlist '{self.name}' of genre '{self.genre}' has been turned into binary usable format/data.")

    def add_song(self, song):
        self.songs.append(song)
        print(f"'{song}' has been added to your playlist as data. '{self.name}'.")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"'{song}' has been removed from your playlist as data. '{self.name}'.")
        else:
            print(f"'{song}' is not in your playlist pls try again moronic entity whose memory is worse than a fictional goldfish '{self.name}'.")

    def display(self):
        print(f"\n--- {self.name} ({self.genre})---")
        for i, song in enumerate(self.songs, 1):
            print(f" {i}. {song}")
        else:
            print("NO SONGS YET ADD SOME NUMNUT")

    def __del__(self):
        print(f"Playlist '{self.name}' Has been relegated and obliterated from the data dimension. RIP")

my_playlist = Playlist("PLAYLIST WAYLIST", "DEVLOPER DOOMSPIRE")

while True:
    print("\n1. Add song  2. remove song 3. view playlist 4.relegate and quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        song = input("Enter the song name: ")
        my_playlist.add_song(song)
    elif choice == "2":
        song = input("Enter the song name to remove: ")
        my_playlist.remove_song(song)
    elif choice == "3":
        my_playlist.display()
    elif choice == "4":
        print("Exiting the playlist manager. Goodbye!")
        del my_playlist
    else:
        print("Invalid choice. Please use 1,2,3,4.")