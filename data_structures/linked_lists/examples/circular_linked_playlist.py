from data_structures.linked_lists.circular_linked_list import CircularLinkedList


class MusicPlaylist:
    def __init__(self):
        self.playlist = CircularLinkedList()

    def add_song(self, song_name):
        self.playlist.append(song_name)
        print(f'Song "{song_name}" added to the playlist.')

    def remove_song(self, song_name):
        self.playlist.delete_node(song_name)
        print(f'Song "{song_name}" removed from the playlist.')

    def show_playlist(self):
        songs = self.playlist.display()
        if songs:
            print("Current Playlist:", " -> ".join(songs))
        else:
            print("The playlist is empty.")


if __name__ == "__main__":
    playlist = MusicPlaylist()
    playlist.add_song("Song 1")
    playlist.add_song("Song 2")
    playlist.add_song("Song 3")
    playlist.show_playlist()  # Output: Current Playlist: Song 1 -> Song 2 -> Song 3
    playlist.remove_song("Song 2")
    playlist.show_playlist()  # Output: Current Playlist: Song 1 -> Song 3
