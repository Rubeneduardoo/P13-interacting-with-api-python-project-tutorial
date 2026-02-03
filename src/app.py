import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# Spotify API credentials
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id = client_id, client_secret= client_secret)
spotify = spotipy.Spotify(auth_manager= auth_manager)

BL = 'spotify:artist:7a0XAaPaK2aDSqa8p3QnC7?'

top10 = spotify.artist_top_tracks(BL)

rolazos = []
fama = []
duracion = []

for pistas in top10['tracks'][0:10]:
    rolazos.append(tracks['name'])
    fama.append(tracks['popularity'])
    duracion.append(tracks['duration_ms'])

data = {
    "Canciones": rolazos,
    "Popularidad": fama,
    "Duracion": duracion
}

df = pd.DataFrame(data)
df