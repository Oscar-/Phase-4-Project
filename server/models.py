from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
class Artist(db.Model, SerializerMixin):
    __tablename__ = "artists"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    gender = db.Column(db.String)
    #birth_date = 
    birth_place = db.Column(db.String)
    biography = db.Column(db.String)


class Song(db.Model, SerializerMixin):
    __tablename__ = "songs"
    id = db.Column(db.Integer, primary_key=True)
    #artist_id = db.Column(db.Integer, )
    length = db.column(db.Integer)
    #release_dt = 
    lyrics = db.Column(db.String)
    genre = db.Column(db.String)
    #photo = db.Column() - insert url


class Review(db.Model, SerializerMixin):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    #song_id = db.Column(db.Integer, )
    #artist_id = db.Column(db.Integer, )
    #user_id = db.Column(db.Integer, )
    rating = db.Column(db.Integer)
    comment = db.Column(db.String)

class Favorite(db.Model, SerializerMixin):
    __tablename__ = "favorites"
    #user_id = db.Column(db.Integer, )
    #artist_id = db.Column(db.Integer, )
    #song_id = db.Column(db.Integer, )