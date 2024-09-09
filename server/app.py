#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, jsonify
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import Artist, Song, Review, Favorite, User

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'


@app.route('/artist', method= ['GET', 'POST'])
def handle_artists():
    if request.method == 'GET':
        # Handle GET request
        artists = Artist.query.all()
        output = []
        for artist in artists:
            artist_data = {'id': artist.id, 'name': artist.name, 'genre': artist.genre}
            output.append(artist_data)
        return jsonify(output)

    elif request.method == 'POST':
        # Handle POST request
        data = request.get_json()
        if 'name' not in data or 'genre' not in data:
            return jsonify({'error': 'Bad request, name and genre are required'}), 400

        new_artist = Artist(name=data['name'], genre=data['genre'])
        db.session.add(new_artist)
        db.session.commit()
        return jsonify({'id': new_artist.id, 'name': new_artist.name, 'genre': new_artist.genre}), 201
    
@app.route('/users', method = ['GET', 'POST'])
def handle_users():
    if request.method == 'GET':
        # Handle GET request
        users = User.query.all()
        output = []
        for user in users:
            user_data = {'id': user.id, 'name': user.name, 'genre': user.genre}
            output.append(user_data)
        return jsonify(output)

    elif request.method == 'POST':
        # Handle POST request
        data = request.get_json()
        if 'name' not in data or 'genre' not in data:
            return jsonify({'error': 'Bad request, name and genre are required'}), 400

        new_user = User(name=data['name'], genre=data['genre'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'id': new_user.id, 'name': new_user.name, 'genre': new_user.genre}), 201

@app.route('/artist/<int:id', method = ['GET', 'DELETE'] )
def artist_by_id(id):
    artist = Artist.query.get(id)

    if request.method == 'GET':
        # Handle GET request
        if artist is None:
            return jsonify({'error': 'Artist not found'}), 404
        artist_data = {'id': artist.id, 'name': artist.name, 'genre': artist.genre}
        return jsonify(artist_data)

    elif request.method == 'DELETE':
        # Handle DELETE request
        if artist is None:
            return jsonify({'error': 'Artist not found'}), 404

        db.session.delete(artist)
        db.session.commit()
        return jsonify({'message': 'Artist deleted successfully'}), 200

@app.route('/user/<int:id', method = ['GET', 'DELETE'])
def user_by_id(id):
    user = User.query.get(id)

    if request.method == 'GET':
        # Handle GET request
        if user is None:
            return jsonify({'error': 'user not found'}), 404
        user_data = {'id': user.id, 'name': user.name, 'genre': user.genre}
        return jsonify(user_data)

    elif request.method == 'DELETE':
        # Handle DELETE request
        if user is None:
            return jsonify({'error': 'User not found'}), 404

        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'user deleted successfully'}), 200
    
@app.route('/song', method = ['GET', 'POST'])
def handle_song():
    if request.method == 'GET':
        # Handle GET request
        song = Artist.query.all()
        output = []
        for song in song:
            song_data = {'id': song.id, 'name': song.name, 'genre': song.genre}
            output.append(song_data)
        return jsonify(output)

    elif request.method == 'POST':
        # Handle POST request
        data = request.get_json()
        if 'name' not in data or 'genre' not in data:
            return jsonify({'error': 'Bad request, name and genre are required'}), 400

        new_song = Song(name=data['name'], genre=data['genre'])
        db.session.add(new_song)
        db.session.commit()
        return jsonify({'id': new_song.id, 'name': new_song.name, 'genre': new_song.genre}), 201

@app.route('/song/<int:id', method = ['GET', 'DELETE'])
def song_by_id(id):
    song = song.query.get(id)

    if request.method == 'GET':
        # Handle GET request
        if song is None:
            return jsonify({'error': 'song not found'}), 404
        song_data = {'id': song.id, 'name': song.name, 'genre': song.genre}
        return jsonify(song_data)

    elif request.method == 'DELETE':
        # Handle DELETE request
        if song is None:
            return jsonify({'error': 'song not found'}), 404

        db.session.delete(song)
        db.session.commit()
        return jsonify({'message': 'song deleted successfully'}), 200


if __name__ == '__main__':
    app.run(port=5555, debug=True)