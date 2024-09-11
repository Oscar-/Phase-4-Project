from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from datetime import datetime
from config import db  # Import db from config

class Artist(db.Model, SerializerMixin):
    __tablename__ = "artists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    birth_date = db.Column(db.Date)
    birth_place = db.Column(db.String)
    biography = db.Column(db.String)
    image = db.Column(db.String)

    # Relationships
    songs = db.relationship('Song', back_populates='artist')
    reviews = db.relationship('Review', back_populates='artist', lazy=True)
    favorites = db.relationship('Favorite', back_populates='artist', lazy=True)

    # Many-to-many relationships
    many_songs = association_proxy('reviews', 'song')

    serialize_rules = ('-reviews.artist', '-favorites.artist', '-favorites.user.reviews', '-favorites.user.favorites')

    @validates('name')
    def validate_name(self, key, value):
        if len(value) < 2:
            raise ValueError('Artist name must be at least 2 characters long')
        return value

    @validates('age')
    def validate_age(self, key, value):
        if value is not None and (value < 0 or value > 120):
            raise ValueError('Age must be between 0 and 120')
        return value

    # @validates('gender')
    # def validate_gender(self, key, value):
    #     if value not in ['Male', 'Female', 'Non-binary', 'Other']:
    #         raise ValueError('Invalid gender')
    #     return value

    def __repr__(self):
        return f'<Artist {self.id}, {self.name}, {self.gender}, {self.birth_place}, {self.biography}>'

class Song(db.Model, SerializerMixin):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    length = db.Column(db.Integer)
    lyrics = db.Column(db.String)
    release_dt = db.Column(db.Date, nullable=False)
    image = db.Column(db.String)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))

    # Relationships
    artist = db.relationship('Artist', back_populates='songs')
    reviews = db.relationship('Review', back_populates='song', lazy=True)
    favorites = db.relationship('Favorite', back_populates='song', lazy=True)

    # Many-to-many relationships
    many_artists = association_proxy('reviews', 'artist')

    serialize_rules = ('-reviews.song', '-favorites.song', '-favorites.user.reviews', '-favorites.user.favorites')

    @validates('name')
    def validate_name(self, key, value):
        if len(value) < 1:
            raise ValueError('Song name must be at least 1 character long')
        return value

    @validates('genre')
    def validate_genre(self, key, value):
        if len(value) < 1:
            raise ValueError('Genre must be at least 1 character long')
        return value

    # @validates('release_dt')
    # def validate_release_date(self, key, value):
    #     if value > datetime.now().date():
    #         raise ValueError('Release date cannot be in the future')
    #     return value

    def __repr__(self):
        return f'<Song {self.id}, {self.name}, {self.genre}, {self.release_dt}>'

class Review(db.Model, SerializerMixin):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    artist = db.relationship('Artist', back_populates='reviews')
    song = db.relationship('Song', back_populates='reviews')
    user = db.relationship('User', back_populates='reviews')

    serialize_rules = ('-artist.reviews', '-song.reviews', '-user.reviews')

    @validates('rating')
    def validate_rating(self, key, value):
        if value < 1 or value > 5:
            raise ValueError('Rating must be between 1 and 5')
        return value

    def __repr__(self):
        return f'<Review {self.id}, {self.rating}, {self.content}, {self.user_id}>'

class Favorite(db.Model, SerializerMixin):
    __tablename__ = "favorites"

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Relationships
    artist = db.relationship('Artist', back_populates='favorites')
    song = db.relationship('Song', back_populates='favorites')
    user = db.relationship('User', back_populates='favorites')

    serialize_rules = ('-artist.favorites', '-song.favorites', '-user.favorites')

    def __repr__(self):
        return f'<Favorite {self.id}, Artist {self.artist_id}, Song {self.song_id}, User {self.user_id}>'

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String)
    bio = db.Column(db.String)

    # Relationships
    reviews = db.relationship('Review', back_populates='user', lazy=True)
    favorites = db.relationship('Favorite', back_populates='user', lazy=True)

    serialize_rules = ('-reviews.user', '-favorites.user')

    # @validates('username')
    # def validate_username(self, key, value):
    #     if len(value) < 3:
    #         raise ValueError('Username must be at least 3 characters long')
    #     return value

    # @validates('email')
    # def validate_email(self, key, value):
    #     if not is_valid_email(value):
    #         raise ValueError('Invalid email address')
    #     return value

    def __repr__(self):
        return f'<User {self.id}, {self.username}, {self.email}>'
