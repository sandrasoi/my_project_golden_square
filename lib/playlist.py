class Playlist():
    def __init__(self, name):
        self.name = name
        self.tracks_listened = []

    def add_track(self, track_name):
        self.tracks_listened.append(track_name)

    def view_tracks(self):
        if self.tracks_listened == []:
            raise Exception("No tracks given")
        else:
            return ', '.join(self.tracks_listened)