from unittest.mock import Mock
from mocking_bites.music_library import *

def test_adding_tracks_and_returning_them():
    music_library = MusicLibrary()
    faketrack1 = Mock()
    music_library.add(faketrack1)
    faketrack2 = Mock()
    music_library.add(faketrack2)
    assert music_library.tracks == [faketrack1, faketrack2]



# testing with fake classes
# def test_adding_tracks_and_returning_them():
#     music_library = MusicLibrary()
#     track1 = FakeTrack1() 
#     track2 = FakeTrack1() 
#     music_library.add(track1)
#     music_library.add(track2)
#     assert music_library.tracks == [track1, track2]



def test_searches_by_keyword():
    music_library = MusicLibrary()
    faketrack1 = Mock()
    music_library.add(faketrack1)
    faketrack2 = Mock()
    music_library.add(faketrack2)
    faketrack1.matches.return_value = True
    faketrack2.matches.return_value = False
    assert music_library.search("hello") == [faketrack1]

#created fake classes
# def test_searches_by_keyword():
#     music_library = MusicLibrary()
#     track1 = FakeTrack1() #contains hello
#     track2 = FakeTrack2() #doesn't contain hello
#     music_library.add(track1)
#     music_library.add(track2)
#     assert music_library.search("hello") == [track1]

# class FakeTrack1():
#     def matches(self, keyword):
#         return True
    
# class FakeTrack2():
#     def matches(self, keyword):
#         return False