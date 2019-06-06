import spotipy
import os
from dotenv import load_dotenv
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri= os.getenv('REDIRECT_URI')
username= os.getenv('USERNAME')

print(username)

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
scope = 'user-library-read playlist-read-private'

try:
    token = util.prompt_for_user_token(username, scope,client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
    spotify = spotipy.Spotify(auth=token)
    playlists = spotify.user_playlists(username)

    for playlist in playlists:
        print(playlist)
except:
    print('Token is not accesible for ' + username)
