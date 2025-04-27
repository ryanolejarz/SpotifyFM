import json
import requests

from config import LAST_FM_BASE_URL
from src.Track import LastFmTrack
from typing import List


BASE_URL = LAST_FM_BASE_URL


class LastFmClient:

    def __init__(self, api_key: str):
        self.base_url = BASE_URL
        self.api_key = api_key
    
    def get_top_tracks(self, user: str) -> List[LastFmTrack]:
        endpoint = "2.0/?method=user.gettoptracks"
        response = requests.post(
            f"{BASE_URL}/{endpoint}&user={user}&api_key={self.api_key}&format=json")
        track_data = json.loads(response.text)["toptracks"]["track"]
        top_tracks: List[LastFmTrack] = []

        # create a top_track object of only the important info and add it to top_tracks list
        for track in track_data:
            top_track = LastFmTrack(
                title=track["name"],
                artist=track["artist"]["name"])
            top_tracks.append(top_track)

        return top_tracks
    

    def get_top_tracks_in_date_range(
            self, 
            user: str, 
            from_date: int, 
            to_date: int, 
            min_plays: int=0, 
            max_tracks: int=100) -> List[LastFmTrack]:
        endpoint = "2.0/?method=user.getweeklytrackchart"
        response = requests.post(
            f"{BASE_URL}/{endpoint}&user={user}"
            f"&api_key={self.api_key}&format=json&from={from_date}&to={to_date}")
        weekly_track_data = json.loads(response.text)["weeklytrackchart"]["track"]

        # create a top_track object of only the important info and add it to top_tracks list
        top_tracks: List[LastFmTrack] = []
        track_count = 0
        for track in weekly_track_data:
            if track_count < max_tracks and int(track["playcount"]) >= min_plays:
                top_track = LastFmTrack(
                    title=track["name"],
                    artist=track["artist"]["#text"])
                top_tracks.append(top_track)
                track_count = track_count + 1

        return top_tracks
