
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from src.Track import SpotifyTrack
from typing import List


class SpotifyClient:

    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.client_credentials_manager = SpotifyClientCredentials(
            self.client_id, self.client_secret)
        self.api = Spotify(client_credentials_manager=self.client_credentials_manager)

    def get_song(self, song_id: str) -> SpotifyTrack:
        # search_results = sp.search(q=f'artist:{artist} track:{song}', type='track', limit=5)
        result = self.api.track(track_id=song_id)
        return result

    def search_song(self, artist: str, song: str) -> List[SpotifyTrack]:
        # search_results = sp.search(q=f'artist:{artist} track:{song}', type='track', limit=5)
        search_results = self.api.search(q=f'{artist} {song}', type='track', limit=5)
        songs: List[SpotifyTrack] = []

        # create a SpotifySong object from the result and add it to songs list
        for result in search_results['tracks']['items']:
            song = SpotifyTrack(
                id=result['id'],
                artist=result['artists'][0]['name'],
                title=result['name']
            )
            songs.append(song)
        
        return songs
