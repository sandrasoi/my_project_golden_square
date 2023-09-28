from mocking_bites.track import*
from mocking_bites.music_library import *

def test_adding_tracks_and_returning_them():
    music_library = MusicLibrary()
    music_library = MusicLibrary()
    track1 = Track("artist", "song") 
    track2 = Track("artist1", "song2") 
    music_library.add(track1)
    music_library.add(track2)
    assert music_library.tracks == [track1, track2]


# def test_searches_by_keyword():
#     music_library = MusicLibrary()
#     track1 = Track("artist", "song hello") 
#     track2 = Track("artist1", "song2") 
#     music_library.add(track1)
#     music_library.add(track2)
#     assert music_library.search("hello") == [track1]
