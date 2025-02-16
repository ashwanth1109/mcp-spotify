# Spotify MCP

A FastMCP tool for Spotify.

## Demo

![Demo](./assets/Demo-v1.mp4)

## Pre-requisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [Spotify API](https://developer.spotify.com/dashboard/applications)

## Installation

- Clone this repository
- Create a `.env` file in the root of the repository and add your Spotify API credentials (copy over from `.env.example`)
- You can get your credentials by going to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and creating an app.
- Go to Cursor Settings > Features > MCP Servers > + Add new MCP server
- Name: Spotify, Type: command, Command: uv --directory <path-to-repository/mcp-spotify> run main.py

You should see the tool installed now.
![installed_mcp](./assets/installed_mcp.png)

## Trying it out

- Open `Composer` in "agent" mode and voila, you can have cursor control your Spotify player. (make sure you have spotify open on an active device)

## Features

Below is an example conversation showcasing how you can interact with the Spotify MCP tool through Cursor Composer:

1. **User:** "Show me my playlists."  
   **Response:** "Here are your playlists: Chill Vibes, Workout Mix, Top Hits."

2. **User:** "Play my 'Chill Vibes' playlist."

3. **User:** "Pause song."  
   **Response:** "Playback paused."

4. **User:** "Resume song."  
   **Response:** "Resuming playback..."

5. **User:** "What song is this?"  
   **Response:** "You're listening to 'Faded' by Alan Walker."

6. **User:** "Tell me about this artist and show me some popular tracks."  
   **Response:** "Artist Info: Alan Walker."

7. **User:** "Show me my top artists from the last 6 months."  
   **Response:** "Here are your most played artists..."

8. **User:** "Search for Coldplay."  
   **Response:** "Found artist: Coldplay. Here are their top tracks..."

9. **User:** "Play song 'Fix You'."  
   **Response:** "Starting playback for 'Fix You'..."

10. **User:** "Show me my queue."  
    **Response:** "Current queue: Track 1, Track 2, Track 3..."

11. **User:** "Add 'Paradise' to my queue."  
    **Response:** "Added 'Paradise' by Coldplay to your queue."

12. **User:** "Move 'Paradise' up in the queue."

13. **User:** "Set it on repeat."

14. **User:** "I like this song. Recommend some similar tracks."  
    **Response:** "Here are some recommendations based on this track..."

15. **User:** "Add this track to my 'Chill Vibes' playlist."

Additional Available Features:
- Seek to specific position in track
- View detailed playback state
- Skip multiple tracks at once

If you want more features to be supported, feel free to raise an issue!

