from datetime import datetime
from config import db
from models import User, Song, Artist
from app import app

# def create_users():
#     with app.app_context():
#         users = [
#             User(
#                 username='Jane Smith',
#                 email='jane.smith@example.com',
#                 password='password123',
#                 image_url='image_url_1.jpg',
#                 bio="John's bio"
#             ),
#             User(
#                 username='Alex Brown',
#                 email='alex.brown@example.com',
#                 password='password456',
#                 image_url='image_url_2.jpg',
#                 bio="Paul's bio"
#             ),
#             User(
#                 username='Sam Green',
#                 email='sam.green@example.com',
#                 password='password789',
#                 image_url='image_url_3.jpg',
#                 bio="Freddie's bio"
#             )
#         ]
#         db.session.bulk_save_objects(users)
#         db.session.commit()

def create_songs():
    with app.app_context():
        songs = [
            # New songs for new artists
            Song(
                name='Stronger',
                genre='Hip-Hop',
                length=305,
                lyrics='That that don’t kill me can only make me stronger',
                release_dt=datetime.strptime('2007-09-11', '%Y-%m-%d'),
                image='stronnger_image.jpg'
            ),
            Song(
                name='Uptown Funk',
                genre='Pop',
                length=269,
                lyrics='Don’t believe me, just watch',
                release_dt=datetime.strptime('2014-11-10', '%Y-%m-%d'),
                image='uptown_funk_image.jpg'
            ),
            Song(
                name='Livin’ on a Prayer',
                genre='Rock',
                length=240,
                lyrics='Woah, we’re halfway there',
                release_dt=datetime.strptime('1986-10-31', '%Y-%m-%d'),
                image='livin_on_a_prayer_image.jpg'
            ),
            Song(
                name='Safaera',
                genre='Reggaeton',
                length=230,
                lyrics='Baby, yo no quiero na’',
                release_dt=datetime.strptime('2020-02-28', '%Y-%m-%d'),
                image='safaera_image.jpg'
            ),
            Song(
                name='No Rest for the Wicked',
                genre='Regional Mexican',
                length=215,
                lyrics='Ya me voy a ir',
                release_dt=datetime.strptime('2022-04-15', '%Y-%m-%d'),
                image='no_rest_for_the_wicked_image.jpg'
            ),
            Song(
                name='HUMBLE.',
                genre='Hip-Hop',
                length=177,
                lyrics='I’m so fuckin’ sick and tired of the Photoshop',
                release_dt=datetime.strptime('2017-03-30', '%Y-%m-%d'),
                image='humble_image.jpg'
            )
        ]
        db.session.bulk_save_objects(songs)
        db.session.commit()

def create_artists():
    with app.app_context():
        artists = [
            # New artists
            Artist(
                name='Kanye West',
                gender='Male',
                age=47,
                birth_date=datetime.strptime('1977-06-08', '%Y-%m-%d'),
                birth_place='Atlanta, Georgia',
                biography='Kanye West is an American rapper, singer, songwriter, record producer, and fashion designer.',
                image='kanye_west_image.jpg'
            ),
            Artist(
                name='Bruno Mars',
                gender='Male',
                age=38,
                birth_date=datetime.strptime('1985-10-08', '%Y-%m-%d'),
                birth_place='Honolulu, Hawaii',
                biography='Bruno Mars is an American singer, songwriter, record producer, and performer.',
                image='bruno_mars_image.jpg'
            ),
            Artist(
                name='Bon Jovi',
                gender='Male',
                age=61,
                birth_date=datetime.strptime('1962-03-02', '%Y-%m-%d'),
                birth_place='Perth Amboy, New Jersey',
                biography='Bon Jovi is an American rock band formed in 1983.',
                image='bon_jovi_image.jpg'
            ),
            Artist(
                name='Bad Bunny',
                gender='Male',
                age=30,
                birth_date=datetime.strptime('1994-03-10', '%Y-%m-%d'),
                birth_place='San Juan, Puerto Rico',
                biography='Bad Bunny is a Puerto Rican singer, rapper, and songwriter.',
                image='bad_bunny_image.jpg'
            ),
            Artist(
                name='Grupo Frontera',
                gender='Group',
                age=None,
                birth_date=None,
                birth_place=None,
                biography='Grupo Frontera is a Mexican regional band.',
                image='grupo_frontera_image.jpg'
            ),
            Artist(
                name='Kendrick Lamar',
                gender='Male',
                age=37,
                birth_date=datetime.strptime('1987-06-17', '%Y-%m-%d'),
                birth_place='Compton, California',
                biography='Kendrick Lamar is an American rapper, songwriter, and record producer.',
                image='kendrick_lamar_image.jpg'
            )
        ]
        db.session.bulk_save_objects(artists)
        db.session.commit()

# def read_users():
#     with app.app_context():
#         return User.query.all()

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

# def update_user(user_id, **kwargs):
#     with app.app_context():
#         user = User.query.get(user_id)
#         if user:
#             for key, value in kwargs.items():
#                 setattr(user, key, value)
#             db.session.commit()

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
    # create_users()
    create_songs()
    create_artists()
