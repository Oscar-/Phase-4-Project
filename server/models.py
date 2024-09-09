from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime, date
from config import db


birthdate = db.Column(db.Date, nullable=False)

# Models go here!
class Artist(db.Model, SerializerMixin):
    __tablename__ = "artists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    gender = db.Column(db.String)
    birth_date = db.Column(db.Date)
    birth_place = db.Column(db.String)
    biography = db.Column(db.String)

    # Relationships
    reviews = db.relationship('Review', backref='artist', lazy=True)
    favorites = db.relationship('Favorite', backref='artist', lazy=True)
    songs = association_proxy('reviews', 'song')  # Proxy relationship to get songs through reviews

    serialize_rules = ('-reviews.artist',)  # Exclude circular references


    def __repr__(self):
        return f'<Artist {self.id}, {self.name}, {self.gender}, {self.birth_place}, {self.biography}'

class Song(db.Model, SerializerMixin):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    length = db.Column(db.Integer)
    lyrics = db.Column(db.String)
    genre = db.Column(db.String)
    # Relationships
    reviews = db.relationship('Review', backref='song', lazy=True)
    artists = association_proxy('reviews', 'artist')  # Proxy relationship to get artists through reviews

    serialize_rules = ('-reviews.song',)  # Exclude circular references

    def __repr__(self):
        return f'<Song {self.id}, {self.length}, {self.lyrics}, {self.genre}, {self.reviews}, {self.artists}'

class Review(db.Model, SerializerMixin):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'))
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    rating = db.Column(db.Integer)
    comment = db.Column(db.String)
    

    def __repr__(self):
        return f'<Artist {self.id}, {self.song_id}, {self.artist_id}, {self.user_id}, {self.rating}, {self.comment}'

class Favorite(db.Model, SerializerMixin):
    __tablename__ = "favorites"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))

    def __repr__(self):
        return f'<Artist {self.id}, {self.user_id}, {self.artist_id}'

class User(db.Model, SerializerMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)

    # Relationships
    reviews = db.relationship('Review', backref='user', lazy=True)
    favorites = db.relationship('Favorite', backref='user', lazy=True)

    serialize_rules = ('-reviews.user', '-favorites.user')  # Exclude circular references

    def __repr__(self):
        return f'<Artist {self.id}, {self.username}, {self.email}'