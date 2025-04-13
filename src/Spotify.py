from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials


class SpotifyClient:

    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.client_credentials_manager = SpotifyClientCredentials(
            self.client_id, self.client_secret)
        self.api = Spotify(client_credentials_manager=self.client_credentials_manager)

    def search_song(self, artist, song):
        client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
        sp = Spotify(client_credentials_manager=self.client_credentials_manager)
        # search_results = sp.search(q=f'artist:{artist} track:{song}', type='track', limit=5)
        search_results = self.api.search(q=f'{artist} {song}', type='track', limit=5)
        songs = []

        # create a song object of only the important info and add it to songs list
        for result in search_results['tracks']['items']:
            song = {}
            song['id'] = result['id']
            song['artist'] = result['artists'][0]['name']
            song['title'] = result['name']
            song['album'] = result['album']['name']
            song['explicit'] = result['explicit']
            songs.append(song)
        
        return songs

    def create_playlist():
        pass