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


@app.route('/artist', methods=['GET', 'POST'])
def handle_artists():
    if request.method == 'GET':
        # Handle GET request
        artists = Artist.query.all()
        output = []
        for artist in artists:
            artist_data = {'id': artist.id, 'name': artist.name, 'gender': artist.gender}
            output.append(artist_data)
        return jsonify(output)

    elif request.method == 'POST':
        # Handle POST request
        data = request.get_json()
        if 'name' not in data or 'gender' not in data:
            return jsonify({'error': 'Bad request, name and gender are required'}), 400

        new_artist = Artist(name=data['name'], gender=data['gender'])
        db.session.add(new_artist)
        db.session.commit()
        return jsonify({'id': new_artist.id, 'name': new_artist.name, 'gender': new_artist.gender}), 201
    
@app.route('/users', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'GET':
        # Handle GET request
        users = User.query.all()
        output = []
        for user in users:
            user_data = {'id': user.id, 'username': user.username, 'email': user.email}
            output.append(user_data)
        return jsonify(output)

    elif request.method == 'POST':
        # Handle POST request
        data = request.get_json()
        if 'username' not in data or 'email' not in data:
            return jsonify({'error': 'Bad request, username and email are required'}), 400

        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'id': new_user.id, 'username': new_user.username, 'email': new_user.email}), 201

@app.route('/artist/<int:id>', methods=['GET', 'DELETE'])
def artist_by_id(id):
    artist = Artist.query.get(id)

    if request.method == 'GET':
        # Handle GET request
        if artist is None:
            return jsonify({'error': 'Artist not found'}), 404
        artist_data = {'id': artist.id, 'name': artist.name, 'gender': artist.gender}
        return jsonify(artist_data)

    elif request.method == 'DELETE':
        # Handle DELETE request
        if artist is None:
            return jsonify({'error': 'Artist not found'}), 404

        db.session.delete(artist)
        db.session.commit()
        return jsonify({'message': 'Artist deleted successfully'}), 200

@app.route('/user/<int:id>', methods=['GET', 'DELETE'])
def user_by_id(id):
    user = User.query.get(id)

    if request.method == 'GET':
        # Handle GET request
        if user is None:
            return jsonify({'error': 'User not found'}), 404
        user_data = {'id': user.id, 'username': user.username, 'email': user.email}
        return jsonify(user_data)

    elif request.method == 'DELETE':
        # Handle DELETE request
        if user is None:
            return jsonify({'error': 'User not found'}), 404

        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    
@app.route('/song', methods=['GET', 'POST'])
def handle_song():
    if request.method == 'GET':
        # Handle GET request
        songs = Song.query.all()
        output = []
        for song in songs:  # Changed from 'song' to 'songs'
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


@app.route('/song/<int:id>', methods=['GET', 'DELETE'])
def song_by_id(id):
    song = Song.query.get(id)

    if request.method == 'GET':
        # Handle GET request
        if song is None:
            return jsonify({'error': 'Song not found'}), 404
        song_data = {'id': song.id, 'name': song.name, 'genre': song.genre}
        return jsonify(song_data)

    elif request.method == 'DELETE':
        # Handle DELETE request
        if song is None:
            return jsonify({'error': 'Song not found'}), 404

        db.session.delete(song)
        db.session.commit()
        return jsonify({'message': 'Song deleted successfully'}), 200


if __name__ == '__main__':
    app.run(port=5555, debug=True)
