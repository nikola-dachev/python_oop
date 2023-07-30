class Music():
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return f'{self.lyrics}'


first_album = Music('Eleno mome', 'Guna Ivanova', '.......')

print(first_album.artist)
print(first_album.print_info())
print(first_album.play())