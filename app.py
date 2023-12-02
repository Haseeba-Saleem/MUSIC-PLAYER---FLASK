from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')


sample_songs = [
    {'name': 'off my face', 'artist': 'Artist 1', 'path': 'OffMyFace.mp3'},
    {'name': 'Ghost', 'artist': 'Artist 2', 'path': 'Ghost.mp3'},
    {'name': 'As I am', 'artist': 'Artist 3', 'path': 'AsIAm.mp3'},
    {'name': 'Ghalat Fehmi', 'artist': 'Artist 3', 'path': 'GhalatFehmi.mp3'},
    {'name': 'Happier Than Ever', 'artist': 'Artist 4', 'path': 'HappierThanEver.mp3'},
    {'name': 'Heather', 'artist': 'Artist 4', 'path': 'Heather.mp3'},
    {'name': 'Die For You', 'artist': 'Artist 5', 'path': 'DieForYou.mp3'},
]



sample_playlists = [
    {'name': 'My Playlist', 'songs': sample_songs[:2]},  
]

sample_artists = [
    {'name': 'Artist 1', 'songs': sample_songs[:1]},  
    {'name': 'Artist 2', 'songs': sample_songs[1:2]},  
    {'name': 'Artist 3', 'songs': sample_songs[2:4]},
    {'name': 'Artist 4', 'songs': sample_songs[4:6]},
    {'name': 'Artist 5', 'songs': sample_songs[6:7]},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/songs')
def songs():
    return render_template('songs.html', songs=sample_songs)

@app.route('/playlists')
def playlists():
    return render_template('playlists.html', playlists=sample_playlists)

@app.route('/artists')
def artists():
    return render_template('artists.html', artists=sample_artists)

if __name__ == '__main__':
    app.run(debug=True)
