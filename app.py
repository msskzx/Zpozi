import spotipy
import os
from dotenv import load_dotenv
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
username= os.getenv('USERNAME')
redirect_uri= os.getenv('REDIRECT_URI')

try:
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    scope = 'user-library-read playlist-read-private'

    token = util.prompt_for_user_token(username, scope,client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
    spotify = spotipy.Spotify(auth=token)

    results = spotify.user_playlists(username)
    playlists = results['items']
    for playlist in playlists:
        print(playlist['name'])
except:
    print('Token is not accesible for ' + username)
