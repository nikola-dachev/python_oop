from typing import Tuple
from project.song import Song

class Album:
  def __init__(self, name: str, *songs: Tuple[Song]):
    self.name = name
    self.published = False
    self.songs = list(songs)


  def add_song(self, song: Song):
    if song in self.songs:
      return "Song is already in the album."

    if self.published == True:
      return "Cannot add songs. Album is published."

    if song.single == True:
      return f"Cannot add {song.name}. It's a single"

    self.songs.append(song)
    return f"Song {song.name} has been added to the album {self.name}."

  def remove_song(self, song_name: str):
    try:
      song = next(filter(lambda x: x.name == song_name, self.songs))


    except StopIteration:
      return "Song is not in the album."

    if self.published == True:
      return "Cannot remove songs. Album is published."

    self.songs.remove(song)
    return f"Removed song {song_name} from album {self.name}."

  def publish(self):
    if self.published == True:
      return f"Album {self.name} is already published."

    self.published = True
    return f"Album {self.name} has been published."


  def details(self):
    song_info = '\n'.join([f"== {s.get_info()}" for s in self.songs])
    return f"Album {self.name}\n" + \
           f"{song_info}"
