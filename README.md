# Music Player

Music Player is a Python desktop music player application built using Tkinter and Pygame, with integration of the Spotify Web API to search songs online.
The application allows users to:
- Import and play local MP3 files
- Search songs online via Spotify
- View search history
- Maintain a playlist of imported songs
- Control playback and volume through a graphical interface

This project demonstrates skills in Python GUI development, API integration, file handling, and multimedia playback.

# Features
## Local Music Playback
- Import songs from a folder
- Play MP3 files using the Pygame mixer
- Maintain a playlist of imported songs

## Spotify Search Integration
- Search for songs using the Spotify Web API
- Automatically opens the song in the user's browser
- Saves search history including:
  - Song name
  - Artist
  - Spotify link

## History & Data Storage
The program stores information using binary files:

- `songs.dat` - imported songs  
- `history.dat` - Spotify search history  
- `info.dat` - project information  

## Graphical User Interface
Built using Tkinter, providing:

- Play / Pause controls  
- Volume adjustment  
- Playlist management  
- Song search field  
- History and imported songs viewer  

# Technologies Used

- **Python**
- **Tkinter** – GUI interface
- **Pygame** – Music playback
- **Spotipy** – Spotify API wrapper
- **PrettyTable** – Display formatted tables
- **Pickle** – Binary data storage

# Spotify API Setup (Required)

This project uses the Spotify Web API to search songs.  
Before running the program, you must create a **Spotify Developer Application**.

## Step 1 – Create a Spotify Developer Account
Go to the Spotify Developer Dashboard:

[https://developer.spotify.com/dashboard/](https://developer.spotify.com/dashboard/)

Log in using your Spotify account and click Create App.

## Step 2 – Get Your Credentials
After creating the app, Spotify will provide a Client ID and Client Secret. Copy these values.

## Step 4 – Add Redirect URI
Inside the Spotify app settings, click Edit Settings and the following redirect URI:

`http://localhost:8888/callback`

Save the settings.

## Step 5 – Replace Placeholders in the Code
Locate this section in the code:

```python
clientID = 'Your client ID'
clientSecret = 'Your client secret'
redirect_url = 'Your redirect url'
```

Replace it with your Spotify credentials:

```python
clientID = 'YOUR_SPOTIFY_CLIENT_ID'
clientSecret = 'YOUR_SPOTIFY_CLIENT_SECRET'
redirect_url = 'http://localhost:8888/callback'
```

# How to Use

## Import Local Music
1. Click Browse Music
2. Select a folder containing `.mp3` files
3. The songs will appear in the playlist panel

## Play Music
1. Select a song from the playlist
2. Click the Play button to start playback

## Search Spotify
1. Enter a song name in the search bar
2. Click Search Online
3. The song will open in your browser via Spotify

## View History
Click the History icon to view previously searched songs.

# Skills Demonstrated

This project highlights experience in:

- **Python GUI development** using Tkinter  
- **API integration** using the Spotify Web API (Spotipy)  
- **File handling and data persistence** using Pickle  
- **Multimedia playback** using the Pygame mixer  
- **Desktop application design and user interface development**  
- **Working with external libraries and APIs**

# Screenshots
![Music Player Interface](https://github.com/cosmo-shi/Music-Player/blob/main/screenshots/Screenshot%202026-03-09%20172648.png)

![Music PLayer playing song from selected directory](https://github.com/cosmo-shi/Music-Player/blob/main/screenshots/Screenshot%202026-03-09%20172722.png)
