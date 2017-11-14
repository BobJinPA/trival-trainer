from flask import Flask, render_template, request, jsonify
from lib.spotapi import SpotApi
from lib.playlist import Playlist
import json
from random import shuffle

app = Flask(__name__)
spotapi = SpotApi()
playlist = Playlist()

@app.route('/')
def form():
    playlist = spotapi.spotify.user_playlists(spotapi.user_id)
    data = {}
    data['list'] = playlist['items']
    return render_template('index.html', data=data)

@app.route('/start', methods=['POST'])
def start():
    # playlist_id = '1KDQUm30fCPeLncWxFVfJz'
    playlist_id = request.form['playlist']
    level = request.form['level']
    tracks = spotapi.spotify.user_playlist_tracks(spotapi.user_id, playlist_id)
    data = {}
    data['playlist_id'] = playlist_id
    track_collection = []
    for track in tracks['items']:
        track_info = {}
        track_info['song_name'] = track['track']['name']
        track_info['song_id'] = track['track']['id']
        track_info['artist_name'] = track['track']['artists'][0]['name']
        track_info['preview'] = track['track']['preview_url']
        if track_info['preview'] != None:
            track_collection.append(track_info)
    data['tracks'] = track_collection
    shuffle(data['tracks'])
    playlist.save_playlist(data)
    return render_template('train.html', data=playlist.data, number=1, level=level)

# @app.route('/start/<playlist_id>', methods=['POST'])
# def start(playlist_id):
#     tracks = spotapi.spotify.user_playlist_tracks(spotapi.user_id, playlist_id)
#     data = {}
#     data['playlist_id'] = playlist_id
#     track_collection = []
#     for track in tracks['items']:
#         track_info = {}
#         track_info['song_name'] = track['track']['name']
#         track_info['song_id'] = track['track']['id']
#         track_info['artist_name'] = track['track']['artists'][0]['name']
#         track_info['preview'] = track['track']['preview_url']
#         if track_info['preview'] != None:
#             track_collection.append(track_info)
#     data['tracks'] = track_collection
#     shuffle(data['tracks'])
#     playlist.save_playlist(data)
#     return render_template('train.html', data=playlist.data, number=1)

@app.route('/train/<number>', methods=['POST'])
def train(number):

    return render_template('train.html', data=playlist.data, number=number, level=level)

@app.route('/summary')
def summary():
    # data = playlist.data
    # return render_template('summary.html', data=data)
    return render_template('summary.html')


# @app.route('/list')
# def list():
#     lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
#     results = spotapi.spotify.artist_top_tracks(lz_uri)
#     # print json.dumps(results, indent=4)
#     # data = len(results['tracks'])
#     data = {}
#     data['len'] = len(results['tracks'])
#     data['value'] = 'Bob'
#
#     return render_template('summary.html', data=data)



# @app.route('/train')
# def t():
#     data = {}
#     data['src'] = "https://p.scdn.co/mp3-preview/e7ea8a13f7caf6942c5447e9cd96aac2a076d85a?cid=1ba46c62b89e4d8ea0c8edc84e756940"
#     return render_template('train.html', data=data, number=1)