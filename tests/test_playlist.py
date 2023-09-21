import pytest
from lib.playlist import*

def test_add_track_reflected_in_list():
    playlist = Playlist("Best songs")
    playlist.add_track("Song 1")
    result = playlist.view_tracks()
    assert result == "Song 1"

def test_several_tracks_reflected_in_list():
    playlist = Playlist("Best songs")
    playlist.add_track("Song 1")
    playlist.add_track("Song 2")
    playlist.add_track("Song 3")
    result = playlist.view_tracks() 
    assert result == "Song 1, Song 2, Song 3"

def test_no_tracks_error():
    playlist = Playlist("Best songs")
    with pytest.raises(Exception) as e:
        playlist.view_tracks()
    error_message = str(e.value)
    assert error_message == "No tracks given"