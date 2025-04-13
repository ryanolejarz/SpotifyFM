from src.Spotify import SpotifyClient
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

client = SpotifyClient(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
print(client.search_song('The Beatles', 'Hey Jude'))
