# File: lib/track.py

class Track:
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title
        # title and artist are both strings
        pass

    def matches(self, keyword):
        if keyword in self.title:
            return True
        
        # keyword is a string
        # Returns true if the keyword matches either the title or artist