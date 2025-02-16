from mcp.server.fastmcp import FastMCP
from spotify import SpotifyClient

mcp = FastMCP("spotify")
client = SpotifyClient()


@mcp.tool()
async def get_my_playlists() -> str:
    """
    FastMCP tool to get user playlists using SpotifyClient.
    """
    return await client.get_my_playlists()


@mcp.tool()
async def start_playback() -> str:
    """
    FastMCP tool to resume playback on the currently active Spotify device.
    """
    return await client.start_playback()


@mcp.tool()
async def pause_playback() -> str:
    """
    FastMCP tool to pause playback on spotify.
    """
    return await client.pause_playback()


@mcp.tool()
async def search_spotify(query: str, type: str = "track", limit: int = 20) -> str:
    """
    Search Spotify for tracks, artists, albums, or playlists.
    Args:
        query: Search term
        type: One of 'track', 'artist', 'album', 'playlist'
        limit: Max number of results
    """
    return await client.search(query, type, limit)


@mcp.tool()
async def next_track() -> str:
    """Skip to next track in queue"""
    return await client.next_track()


@mcp.tool()
async def previous_track() -> str:
    """Go back to previous track"""
    return await client.previous_track()


@mcp.tool()
async def seek_position(position_ms: int) -> str:
    """
    Seek to position in current track
    Args:
        position_ms: Position in milliseconds
    """
    return await client.seek_track(position_ms)


@mcp.tool()
async def get_playback_state() -> str:
    """Get current playback information"""
    return await client.get_current_playback()


@mcp.tool()
async def get_recommendations(
    seed_artists: str = None,
    seed_tracks: str = None,
    seed_genres: str = None,
    limit: int = 20,
) -> str:
    """
    Get Spotify recommendations based on seeds
    Args:
        seed_artists: Comma-separated artist IDs
        seed_tracks: Comma-separated track IDs
        seed_genres: Comma-separated genres
        limit: Number of recommendations
    """
    return await client.recommendations(seed_artists, seed_tracks, seed_genres, limit)


@mcp.tool()
async def get_item_info(item_id: str, type: str = "track") -> str:
    """
    Get detailed information about a Spotify item
    Args:
        item_id: Spotify ID
        type: One of 'track', 'album', 'artist', 'playlist'
    """
    return await client.get_info(item_id, type)


@mcp.tool()
async def start_playback_track(track_uri: str, device_id: str = None) -> str:
    """
    Start playback of a specific track on Spotify
    Args:
        track_uri: Spotify URI of the track (e.g. 'spotify:track:1234...')
        device_id: Optional device to play on
    """
    return await client.start_playback_track(track_uri, device_id)


@mcp.tool()
async def get_top_artists(limit: int = 20, time_range: str = "medium_term") -> str:
    """
    Get user's top artists from Spotify
    Args:
        limit: Number of artists (max 50)
        time_range: One of 'short_term' (4 weeks), 'medium_term' (6 months), 'long_term' (all time)
    """
    return await client.get_top_artists(limit, time_range)


@mcp.tool()
async def get_queue() -> str:
    """Get the current queue of tracks"""
    return await client.get_queue()


@mcp.tool()
async def add_to_queue(track_id: str) -> str:
    """
    Add a track to the queue
    Args:
        track_id: Spotify track ID to add
    """
    return await client.add_to_queue(track_id)


@mcp.tool()
async def skip_tracks(num_skips: int = 1) -> str:
    """
    Skip multiple tracks at once
    Args:
        num_skips: Number of tracks to skip (default: 1)
    """
    return await client.skip_track(num_skips)


@mcp.tool()
async def get_current_track() -> str:
    """Get information about the currently playing track"""
    return await client.get_current_track()


@mcp.tool()
async def start_playlist_playback(playlist_id: str, device_id: str = None) -> str:
    """
    Start playback of a specific playlist
    Args:
        playlist_id: Spotify playlist ID
        device_id: Optional device to play on
    """
    return await client.start_context_playback(
        f"spotify:playlist:{playlist_id}", device_id
    )


@mcp.tool()
async def get_artist_top_tracks(artist_id: str) -> str:
    """
    Get top tracks for an artist
    Args:
        artist_id: Spotify artist ID
    """
    return await client.get_artist_top_tracks(artist_id)


@mcp.tool()
async def set_repeat_mode(state: str) -> str:
    """
    Set repeat mode for playback
    Args:
        state: One of 'track', 'context', or 'off'
    """
    return await client.set_repeat(state)


@mcp.tool()
async def add_to_playlist(playlist_id: str, track_ids: list[str]) -> str:
    """
    Add tracks to a playlist
    Args:
        playlist_id: Spotify playlist ID
        track_ids: List of track IDs to add
    """
    return await client.add_to_playlist(playlist_id, track_ids)


@mcp.tool()
async def reorder_queue(range_start: int, insert_before: int) -> str:
    """
    Reorder tracks in queue by moving a track to a different position
    Args:
        range_start: Position of track to move
        insert_before: Position to insert the track
    """
    return await client.reorder_queue(range_start, insert_before)


def main() -> None:
    print("MCP Spotify Running...")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
