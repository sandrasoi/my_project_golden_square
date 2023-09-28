from mocking_bites.track import Track

def test_matches_if_keyword_in_title():
    track = Track("artist", "hello song")
    result = track.matches("hello")
    assert result == True