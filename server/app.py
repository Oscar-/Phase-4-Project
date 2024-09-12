from flask import Flask, request, jsonify
from config import app, db
from models import Artist, Song, Review, Favorite, User
from flask_cors import CORS
from datetime import datetime
import logging

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

            # Convert 'birth_date' string to a Python date object
            birth_date = datetime.strptime(data['birth_date'], '%d-%m-%y').date()

            new_artist = Artist(
                name=data['name'],
                gender=data['gender'],
                birth_date=birth_date,
                birth_place=data.get('birth_place'),
                biography=data.get('biography'),
                image=data.get('image'),
                age=data.get('age')  # Optional
            )
            db.session.add(new_artist)
            db.session.commit()
            return jsonify(new_artist.to_dict()), 201
        except ValueError as ve:
            return jsonify({'error': f"Invalid date format: {ve}"}), 400
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error occurred during POST: {e}")
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
    print(f"Requested ID: {id}, Artist Found: {artist}")  # Add logging
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
            print(f"Received data: {data}")  # Debug statement

            required_fields = ['name', 'genre', 'release_dt']
            if not all(field in data for field in required_fields):
                return jsonify({'error': 'Bad request, name, genre, and release_dt are required'}), 400

            try:
                release_dt = datetime.strptime(data['release_dt'], '%Y-%m-%d').date()
            except ValueError:
                return jsonify({'error': 'Invalid date format'}), 400

            new_song = Song(
                name=data['name'],
                genre=data['genre'],
                length=data.get('length'),
                lyrics=data.get('lyrics'),
                release_dt=release_dt,
                image=data.get('image'),
                artist_id=data.get('artist_id')
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
    
@app.route('/reviews/<int:review_id>', methods=['GET'])
def get_review(review_id):
    review = Review.query.get(review_id)
    if review:
        return jsonify(review.to_dict())
    return {'message': 'Review not found'}, 404

@app.route('/reviews', methods=['POST'])
def create_review():
    parser = request.get_json()
    content = parser.get('content')
    rating = parser.get('rating')
    artist_id = parser.get('artist_id')
    song_id = parser.get('song_id')
    user_id = parser.get('user_id')

    if not content or not rating or not artist_id or not song_id or not user_id:
        return {'message': 'Missing required fields'}, 400

    try:
        review = Review(
            content=content,
            rating=rating,
            artist_id=artist_id,
            song_id=song_id,
            user_id=user_id
        )
        db.session.add(review)
        db.session.commit()
        return jsonify(review.to_dict())
    except Exception as e:
        return {'message': str(e)}, 400

@app.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        return {'message': 'Review not found'}, 404

    data = request.get_json()
    content = data.get('content')
    rating = data.get('rating')
    artist_id = data.get('artist_id')
    song_id = data.get('song_id')
    user_id = data.get('user_id')

    if content:
        review.content = content
    if rating:
        review.rating = rating
    if artist_id:
        review.artist_id = artist_id
    if song_id:
        review.song_id = song_id
    if user_id:
        review.user_id = user_id

    try:
        db.session.commit()
        return jsonify(review.to_dict())
    except Exception as e:
        return {'message': str(e)}, 400

@app.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        return {'message': 'Review not found'}, 404

    try:
        db.session.delete(review)
        db.session.commit()
        return {'message': 'Review deleted'}, 204
    except Exception as e:
        return {'message': str(e)}, 400

if __name__ == '__main__':
    app.run(port=5555, debug=True)