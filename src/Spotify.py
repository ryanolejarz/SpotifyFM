
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from src.Track import SpotifyTrack
from typing import List


class SpotifyClient:

    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, scope: str) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.client_credentials_manager = SpotifyClientCredentials(
            self.client_id, self.client_secret)
        self.api = Spotify(client_credentials_manager=self.client_credentials_manager)
        self._authenticate_user()

    def _authenticate_user(self) -> None:
        self.auth_manager = SpotifyOAuth(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri,
            scope=self.scope,
        )
        self.api = Spotify(auth_manager=self.auth_manager)

    def get_song(self, song_id: str) -> SpotifyTrack:
        """ returns a SpotifyTrack for a given spotify song id """
        result = self.api.track(track_id=song_id)
        return result

    def search_song(self, artist: str, song: str) -> List[SpotifyTrack]:
        search_results = self.api.search(q=f'{artist} {song}', type='track', limit=5)
        songs: List[SpotifyTrack] = []

        # create a SpotifyTrack object from the result and add it to songs list
        for result in search_results['tracks']['items']:
            song = SpotifyTrack(
                id=result['id'],
                artist=result['artists'][0]['name'],
                title=result['name']
            )
            songs.append(song)

        return songs

    def create_playlist(self, username: str, playlist_name: str, description: str, public: bool = True) -> str:
        playlist = self.api.user_playlist_create(
            user=self.api.user(username)['id'],
            name=playlist_name,
            description=description,
            public=public)
        return playlist['id']

    def add_tracks_to_playlist(self, playlist_id: str, track_ids: List[str]) -> None:
        self.api.user_playlist_add_tracks(
            user=self.api.current_user()['id'],
            playlist_id=playlist_id,
            tracks=track_ids
        )
        return None

    def get_user_playlists(self) -> List[dict]:
        """ Fetches the current user's playlists """
        playlists = []
        results = self.api.current_user_playlists(limit=50)  # Get up to 50 playlists
        for playlist in results['items']:
            playlists.append({
                'name': playlist['name'],
                'id': playlist['id'],
                'url': playlist['external_urls']['spotify']
            })
        return playlists
