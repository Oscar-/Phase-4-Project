from datetime import datetime
from config import db
from models import User, Song, Artist
from app import app

def create_users():
    with app.app_context():
        users = [
            User(
                username='Jane Smith',
                email='jane.smith@example.com',
                password='password123',
                image_url='image_url_1.jpg',
                bio="John's bio"
            ),
            User(
                username='Alex Brown',
                email='alex.brown@example.com',
                password='password456',
                image_url='image_url_2.jpg',
                bio="Paul's bio"
            ),
            User(
                username='Sam Green',
                email='sam.green@example.com',
                password='password789',
                image_url='image_url_3.jpg',
                bio="Freddie's bio"
            )
        ]
        db.session.bulk_save_objects(users)
        db.session.commit()

def create_songs():
    with app.app_context():
        songs = [
            Song(
                name='Imagine',
                genre='Rock',
                length=180,
                lyrics='Imagine all the people',
                release_dt=datetime.strptime('1971-10-11', '%Y-%m-%d'),
                image='song_image_1.jpg'
            ),
            Song(
                name='Hey Jude',
                genre='Rock',
                length=240,
                lyrics='Hey Jude',
                release_dt=datetime.strptime('1968-08-26', '%Y-%m-%d'),
                image='song_image_2.jpg'
            ),
            Song(
                name='Bohemian Rhapsody',
                genre='Rock',
                length=354,
                lyrics='Is this the real life?',
                release_dt=datetime.strptime('1975-10-31', '%Y-%m-%d'),
                image='song_image_3.jpg'
            )
        ]
        db.session.bulk_save_objects(songs)
        db.session.commit()

def create_artists():
    with app.app_context():
        artists = [
            Artist(
                name='John Doe',
                gender='Male',
                age=53,
                birth_date=datetime.strptime('1970-01-01', '%Y-%m-%d'),
                birth_place='New York City',
                biography="John's bio",
                image='image_url_1.jpg'
            ),
            Artist(
                name='Paul McCartney',
                gender='Male',
                age=81,
                birth_date=datetime.strptime('1942-06-18', '%Y-%m-%d'),
                birth_place='Liverpool',
                biography="Paul's bio",
                image='image_url_2.jpg'
            ),
            Artist(
                name='Freddie Mercury',
                gender='Male',
                age=77,
                birth_date=datetime.strptime('1946-09-05', '%Y-%m-%d'),
                birth_place='Zanzibar',
                biography="Freddie's bio",
                image='image_url_3.jpg'
            )
        ]
        db.session.bulk_save_objects(artists)
        db.session.commit()

def read_users():
    with app.app_context():
        return User.query.all()

def read_songs():
    with app.app_context():
        return Song.query.all()

def read_artists():
    with app.app_context():
        return Artist.query.all()

def delete_users():
    with app.app_context():
        User.query.delete()
        db.session.commit()

def delete_songs():
    with app.app_context():
        Song.query.delete()
        db.session.commit()

def delete_artists():
    with app.app_context():
        Artist.query.delete()
        db.session.commit()

def update_user(user_id, **kwargs):
    with app.app_context():
        user = User.query.get(user_id)
        if user:
            for key, value in kwargs.items():
                setattr(user, key, value)
            db.session.commit()

def update_song(song_id, **kwargs):
    with app.app_context():
        song = Song.query.get(song_id)
        if song:
            for key, value in kwargs.items():
                setattr(song, key, value)
            db.session.commit()

def update_artist(artist_id, **kwargs):
    with app.app_context():
        artist = Artist.query.get(artist_id)
        if artist:
            for key, value in kwargs.items():
                setattr(artist, key, value)
            db.session.commit()

if __name__ == '__main__':
    create_users()
    create_songs()
    create_artists()
