import os
from typing import Optional
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

# Constants
SPOTIFY_API_BASE = "https://api.spotify.com/v1"

# Spotify setup
SCOPES = [
    "user-read-currently-playing",
    "user-read-playback-state",
    "user-read-currently-playing",  # spotify connect
    "app-remote-control",
    "streaming",  # playback
    "playlist-read-private",
    "playlist-read-collaborative",
    "playlist-modify-private",
    "playlist-modify-public",
    # playlists
    "user-read-playback-position",
    "user-top-read",
    "user-read-recently-played",  # listening history
    "user-library-modify",
    "user-library-read",  # library
]


class SpotifyClient:
    """
    A class that encapsulates all Spotify API functionality.
    """

    def __init__(self) -> None:
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=os.getenv("SPOTIFY_CLIENT_ID"),
                client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
                redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
                scope=SCOPES,
            )
        )

    async def get_my_playlists(self) -> str:
        """
        Get all playlists for the current user.
        """
        try:
            results = self.sp.current_user_playlists()
            if not results["items"]:
                return "No playlists found."

            playlists = []
            for item in results["items"]:
                name = item["name"].encode("ascii", "ignore").decode()
                playlist = (
                    f"Name: {name}\n"
                    f"Tracks: {item['tracks']['total']}\n"
                    f"ID: {item['id']}"
                )
                playlists.append(playlist)
            return "\n---\n".join(playlists)
        except Exception as e:
            return f"Error fetching playlists: {str(e)}"

    async def start_playback(self, device_id: Optional[str] = None) -> str:
        """
        Start or resume playback on the specified device.
        """
        try:
            self.sp.start_playback(device_id=device_id)
            return "Playback started successfully"
        except Exception as e:
            return f"Error starting playback: {str(e)}"

    async def pause_playback(self) -> str:
        """
        Pause playback on the specified device.
        """
        try:
            self.sp.pause_playback()
            return "Playback paused successfully"
        except Exception as e:
            return f"Error pausing playback: {str(e)}"

    async def recommendations(
        self,
        seed_artists: Optional[str] = None,
        seed_tracks: Optional[str] = None,
        seed_genres: Optional[str] = None,
        limit: int = 20,
    ) -> dict:
        """
        Get recommendations based on seed artists, tracks, or genres.
        """
        try:
            recommendations = self.sp.recommendations(
                seed_artists=seed_artists,
                seed_tracks=seed_tracks,
                seed_genres=seed_genres,
                limit=limit,
            )
            return recommendations
        except Exception as e:
            return f"Error getting recommendations: {str(e)}"

    async def get_info(
        self,
        item_id: str,
        qtype: str = "track",
    ) -> dict:
        """
        Get information about a specific item.
        - item_id: id.
        - qtype: Either "track", "album", "artist", or "playlist".
        """
        try:
            match qtype:
                case "track":
                    return self.sp.track(item_id)
                case "album":
                    return self.sp.album(item_id)
                case "artist":
                    return self.sp.artist(item_id)
                case "playlist":
                    return self.sp.playlist(item_id)

            raise ValueError(f"Invalid query type: {qtype}")
        except Exception as e:
            return f"Error getting information: {str(e)}"

    async def search(self, query: str, qtype: str = "track", limit: int = 20) -> dict:
        """
        Search for tracks, artists, albums, or playlists.
        - query: Search query
        - qtype: Either "track", "artist", "album", or "playlist"
        - limit: Max number of results (default 20)
        """
        try:
            results = self.sp.search(q=query, type=qtype, limit=limit)
            return results
        except Exception as e:
            return f"Error searching: {str(e)}"

    async def get_current_playback(self) -> str:
        """
        Get information about current playback state.
        """
        try:
            playback = self.sp.current_playback()
            if not playback:
                return "No active playback session."
            return playback
        except Exception as e:
            return f"Error getting playback state: {str(e)}"

    async def next_track(self) -> str:
        """
        Skip to the next track.
        """
        try:
            self.sp.next_track()
            return "Skipped to next track"
        except Exception as e:
            return f"Error skipping track: {str(e)}"

    async def previous_track(self) -> str:
        """
        Skip to the previous track.
        """
        try:
            self.sp.previous_track()
            return "Skipped to previous track"
        except Exception as e:
            return f"Error skipping track: {str(e)}"

    async def seek_track(self, position_ms: int) -> str:
        """
        Seek to position in currently playing track.
        - position_ms: Position in milliseconds
        """
        try:
            self.sp.seek_track(position_ms=position_ms)
            return f"Seeked to position {position_ms}ms"
        except Exception as e:
            return f"Error seeking: {str(e)}"

    async def start_playback_track(
        self, 
        track_uri: str, 
        device_id: Optional[str] = None
    ) -> str:
        """
        Start playback of a specific track.
        - track_uri: Spotify URI of the track to play
        - device_id: Optional device to play on
        """
        try:
            self.sp.start_playback(
                device_id=device_id,
                uris=[track_uri]
            )
            return "Started playing track successfully"
        except Exception as e:
            return f"Error starting track playback: {str(e)}"

    async def get_top_artists(self, limit: int = 20, time_range: str = "medium_term") -> dict:
        """
        Get the current user's top artists.
        - limit: Number of artists to return (default 20, max 50)
        - time_range: 'short_term' (last 4 weeks), 'medium_term' (last 6 months), 
                     or 'long_term' (all time) (default: medium_term)
        """
        try:
            results = self.sp.current_user_top_artists(
                limit=limit,
                offset=0,
                time_range=time_range
            )
            return results
        except Exception as e:
            return f"Error getting top artists: {str(e)}"

    async def get_queue(self) -> dict:
        """
        Get the current user's queue.
        Returns information about the queue including currently playing track and next tracks.
        """
        try:
            results = self.sp.queue()
            return results
        except Exception as e:
            return f"Error getting queue: {str(e)}"

    async def add_to_queue(self, track_id: str) -> str:
        """
        Add a track to the user's queue.
        - track_id: Spotify track ID to add
        """
        try:
            self.sp.add_to_queue(uri=f"spotify:track:{track_id}")
            return "Track added to queue successfully"
        except Exception as e:
            return f"Error adding track to queue: {str(e)}"

    async def skip_track(self, n: int = 1) -> str:
        """
        Skip multiple tracks in the queue.
        - n: Number of tracks to skip (default: 1)
        """
        try:
            for _ in range(n):
                self.sp.next_track()
            return f"Skipped {n} tracks successfully"
        except Exception as e:
            return f"Error skipping tracks: {str(e)}"

    async def get_current_track(self) -> dict:
        """
        Get detailed information about the currently playing track.
        Returns None if no track is currently playing.
        """
        try:
            result = self.sp.current_user_playing_track()
            if not result:
                return "No track currently playing"
            return result
        except Exception as e:
            return f"Error getting current track: {str(e)}"

    