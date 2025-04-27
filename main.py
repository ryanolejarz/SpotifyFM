from config import LAST_FM_API_KEY, LAST_FM_USER, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
from datetime import datetime
from src.LastFm import LastFmClient
from src.Track import LastFmTrack, SpotifyTrack
from src.Spotify import SpotifyClient
from typing import List


lastfm = LastFmClient(LAST_FM_API_KEY)
spotify = SpotifyClient(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
songs: List[SpotifyTrack] = spotify.search_song('The Beatles', 'Hey Jude')
top_tracks: List[LastFmTrack] = lastfm.get_top_tracks(LAST_FM_USER)


top_tracks_in_range = lastfm.get_top_tracks_in_date_range(
    LAST_FM_USER,
    FROM = int(round(datetime(2013, 1, 1).timestamp())),
    TO = int(round(datetime(2013, 4, 11).timestamp())),
    min_plays=1,
    max_tracks=25
)

print("Top Tracks in Range:")
for track in top_tracks_in_range:
    print(track)
