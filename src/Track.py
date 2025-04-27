from typing import List


class Track:
    def __init__(self, title: str, artist: str):
        self.title = title
        self.artist = artist

    def __str__(self):
        return f"{self.artist} - {self.title}"


class SpotifyTrack(Track):
    def __init__(self, title: str, artist: str, id: str):
        super().__init__(title, artist)
        self.id = id

    def __str__(self):
        return f"{self.artist} - {self.title} ({self.id})"


class LastFmTrack(Track):
    def __init__(self, title: str, artist: str, spotify_matches: List[SpotifyTrack] = []):
        super().__init__(title, artist)
        self.spotify_matches = spotify_matches

    def __str__(self):
        return super().__str__()

    def add_spotify_match(self, track_id: str) -> None:
        self.spotify_matches.append(track_id)
