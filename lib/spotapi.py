from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

class SpotApi:
    def __init__(self):
        client_id = "1ba46c62b89e4d8ea0c8edc84e756940"
        client_secret = "9845917ab5e647adab333f5f50e0774c"
        client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        self.spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        self.user_id = 1293513756


    # def create_test(self, playlist):
    #     data = {}
    #     return data
