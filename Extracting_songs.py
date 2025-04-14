import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


client_id = "your_client_id"
client_secret = "your_client_secret"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager, requests_timeout=100)

df = pd.read_excel('/Users/komalb/Downloads/Personality results.xlsx')
user_ids = df['Profile_id']
user_ids.dropna(inplace=True)

data_dict = {"User id":[], "Playlist Name":[], "Playlist id":[], "Song Name":[], "Song id":[], "Album":[],
             "Artist(s)":[], "Duration(ms)":[], "Popularity":[], "Danceability":[], "Energy":[], "Key":[], "Loudness":[],"Mode":[], "Speechiness":[], "Acousticness":[], "Instrumentalness":[], "Liveness":[], "Valence":[],"Tempo":[]}
res = []

for user in user_ids:
    user_playlist_items = sp.user_playlists(user)['items']
    if user_playlist_items:
        for playlist in user_playlist_items:
            playlist_id = playlist['id']
            playlist_name = playlist['name']
            playlist_tracks = sp.playlist_tracks(playlist_id)
            track_items = playlist_tracks['items']
            if track_items:
                for item in track_items:
                    temp_lst = []
                    track = item['track']
                    if track and track['id']:
                        features = sp.audio_features(track['id'])
                        if features and features[0]:
                            features = features[0]
                            temp_lst.append([user, playlist_name, playlist_id, track['name'], track['id'], track['album']['name'],
                                         track['artists'][0]['name'], track['duration_ms'], track['popularity'],
                             features['danceability'], features['energy'], features['key'], features['loudness'], features['mode'], features['speechiness'], features['acousticness'], features['instrumentalness'], features['liveness'], features['valence'], features['tempo']])

                        else:
                            temp_lst.append(
                                [user, playlist_name, playlist_id, track['name'], track['id'], track['album']['name'],
                                 track['artists'][0]['name'], track['duration_ms'], track['popularity'],
                                 None, None, None, None, None, None, None, None, None, None, None])

                        for idx,ele in enumerate(data_dict):
                            data_dict[ele].append(temp_lst[0][idx])


extracted_data_df = pd.DataFrame(data_dict)

print(extracted_data_df)

extracted_data_df.to_excel('/Users/komalb/Downloads/Songs_new.xlsx')
