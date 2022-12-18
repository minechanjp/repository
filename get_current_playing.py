import time

import spotipy
import spotipy.util as util

client_id = 'your_client_id'
client_secret = 'your_secret_id'
redirect_uri = 'your_redirect_url'
scope = 'user-read-currently-playing'
username = 'your_username'


def get_current_playing():
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_playing_track()
        links = results['context']['external_urls']['spotify']
        artist = results['item']['artists'][0]['name']
        print("=========================================================================\n")
        print(f"Artist :        {artist}")
        print(f"                {links}\n")
        print(f"Playing song :  {results['item']['name']}\n")
        print(f"Album :         {results['item']['album']['name']}\n")
        print("=========================================================================\n")

    else:
        print("Can't get token for", username)


get_current_playing()
