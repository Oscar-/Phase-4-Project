from flask import Flask, request, jsonify
from config import app, db
from models import Artist, Song, Review, Favorite, User
from flask_cors import CORS

# Allow CORS for all routes
CORS(app)

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

@app.route('/artist', methods=['GET', 'POST'])


def handle_artists():
    if request.method == 'GET':
        try:
            artists = Artist.query.all()
            output = [artist.to_dict(only=('id', 'name', 'age', 'gender', 'birth_date', 'birth_place', 'biography', 'image')) for artist in artists]
            return jsonify(output)
        except Exception as e:
            print(f"Error occurred during GET: {e}")
            return jsonify({'error': 'Internal Server Error'}), 500

    elif request.method == 'POST':
        try:
            data = request.get_json(force=True)
            required_fields = ['name', 'gender', 'birth_date']
            if not all(field in data for field in required_fields):
                return jsonify({'error': 'Bad request, name, gender, and birth_date are required'}), 400
            new_artist = Artist(
                name=data['name'],
                gender=data['gender'],
                birth_date=data.get('birth_date'),
                birth_place=data.get('birth_place'),
                biography=data.get('biography'),
                image=data.get('image')
            )
            db.session.add(new_artist)
            db.session.commit()
            return jsonify(new_artist.to_dict()), 201
        except Exception as e:
            print(f"Error occurred during POST: {e}")
            return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/users', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'GET':
        try:
            users = User.query.all()
            output = [user.to_dict() for user in users]
            return jsonify(output)
        except Exception as e:
            print(f"Error occurred during GET: {e}")
            return jsonify({'error': 'Internal Server Error'}), 500
    elif request.method == 'POST':
        try:
            data = request.get_json(force=True)
            required_fields = ['username', 'email', 'password']
            if not all(field in data for field in required_fields):
                return jsonify({'error': 'Bad request, username, email, and password are required'}), 400
            new_user = User(
                username=data['username'],
                email=data['email'],
                password=data['password']
            )
            db.session.add(new_user)
            db.session.commit()
            return jsonify(new_user.to_dict()), 201
        except Exception as e:
            print(f"Error occurred during POST: {e}")
            return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/artist/<int:id>', methods=['GET', 'DELETE'])
def artist_by_id(id):
    artist = Artist.query.get(id)
    if request.method == 'GET':
        if artist is None:
            return jsonify({'error': 'Artist not found'}), 404
        return jsonify(artist.to_dict())
    elif request.method == 'DELETE':
        if artist is None:
            return jsonify({'error': 'Artist not found'}), 404
        db.session.delete(artist)
        db.session.commit()
        return jsonify({'message': 'Artist deleted successfully'}), 200

@app.route('/user/<int:id>', methods=['GET', 'DELETE'])
def user_by_id(id):
    user = User.query.get(id)
    if request.method == 'GET':
        if user is None:
            return jsonify({'error': 'User not found'}), 404
        return jsonify(user.to_dict())
    elif request.method == 'DELETE':
        if user is None:
            return jsonify({'error': 'User not found'}), 404
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200

@app.route('/song', methods=['GET', 'POST'])
def handle_songs():
    if request.method == 'GET':
        try:
            songs = Song.query.all()
            output = [song.to_dict(only=('id', 'name', 'genre', 'length', 'lyrics', 'release_dt', 'image')) for song in songs]
            return jsonify(output)
        except Exception as e:
            print(f"Error occurred during GET: {e}")
            return jsonify({'error': 'Internal Server Error'}), 500
    elif request.method == 'POST':
        try:
            data = request.get_json(force=True)
            required_fields = ['name', 'genre', 'release_dt']
            if not all(field in data for field in required_fields):
                return jsonify({'error': 'Bad request, name, genre, and release_dt are required'}), 400
            new_song = Song(
                name=data['name'],
                genre=data['genre'],
                length=data.get('length'),
                lyrics=data.get('lyrics'),
                release_dt=data['release_dt'],
                image=data.get('image')
            )
            db.session.add(new_song)
            db.session.commit()
            return jsonify(new_song.to_dict()), 201
        except Exception as e:
            print(f"Error occurred during POST: {e}")
            return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/song/<int:id>', methods=['GET', 'DELETE'])
def song_by_id(id):
    song = Song.query.get(id)
    if request.method == 'GET':
        if song is None:
            return jsonify({'error': 'Song not found'}), 404
        return jsonify(song.to_dict())
    elif request.method == 'DELETE':
        if song is None:
            return jsonify({'error': 'Song not found'}), 404
        db.session.delete(song)
        db.session.commit()
        return jsonify({'message': 'Song deleted successfully'}), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)