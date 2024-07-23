class SongNode:
    def __init__(self, song, next=None):
        self.song = song
        self.next = next
        self.prev = None


class Playlist:
    def __init__(self) -> None:
        self.head: SongNode | None = None

    def is_empty(self) -> bool:
        return self.head is None

    def add_song(self, song: str) -> None:
        new_song = SongNode(song)

        if self.is_empty():
            self.head = new_song
            return

        current_song = self.head
        while current_song.next is not None:
            current_song = current_song.next

        current_song.next = new_song
        new_song.prev = current_song

    def remove_song(self, song: str) -> None:
        if self.is_empty():
            return

        # If the song to remove is the first song
        if self.head.song == song:
            if self.head.next is not None:
                self.head.next.prev = None

            self.head = self.head.next
            return

        current_song = self.head

        while current_song.next is not None:
            # If the song to remove is the next song of the current song being checked
            if current_song.next.song == song:
                # remove the next song
                current_song.next = current_song.next.next
                # If the next song is not the last song
                if current_song.next is not None:
                    current_song.next.prev = current_song
                return

            current_song = current_song.next

    def display_songs(self) -> None:
        if self.is_empty():
            print("The playlist is empty")
            return

        current_song = self.head
        while current_song is not None:
            print(current_song.song)
            current_song = current_song.next


SONG_4 = "Song 4"

if __name__ == "__main__":
    playlist = Playlist()
    playlist.add_song("Song 1")
    playlist.add_song("Song 2")
    playlist.add_song("Song 3")
    playlist.add_song(SONG_4)
    playlist.add_song("Song 5")
    playlist.display_songs()
    print()
    playlist.remove_song("Song 3")
    playlist.display_songs()
    print()
    playlist.remove_song("Song 1")
    playlist.display_songs()
    print()
    playlist.remove_song("Song 5")
    playlist.display_songs()
    print()
    playlist.remove_song("Song 2")
    playlist.display_songs()
    print()
    playlist.remove_song(SONG_4)
    playlist.display_songs()
    print()
    playlist.remove_song(SONG_4)
    playlist.display_songs()
