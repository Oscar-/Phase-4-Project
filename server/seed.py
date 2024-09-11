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


def create_artists():
    with app.app_context():
        artist1 = Artist(
            name='Kanye West',
            gender='Male',
            age=47,
            birth_date=datetime.strptime('1977-06-08', '%Y-%m-%d'),
            birth_place='Atlanta, Georgia',
            biography='Kanye West is an American rapper, singer, songwriter, record producer, and fashion designer.',
            image='https://th.bing.com/th/id/OIP.67bxlko6Hc-JdgDEFP5RaQHaE8?rs=1&pid=ImgDetMain'
        )
        artist2 = Artist(
            name='Bruno Mars',
            gender='Male',
            age=38,
            birth_date=datetime.strptime('1985-10-08', '%Y-%m-%d'),
            birth_place='Honolulu, Hawaii',
            biography='Bruno Mars is an American singer, songwriter, record producer, and performer.',
            image='https://wallpapers.com/images/hd/close-up-portrait-of-bruno-mars-yzscqx02tb4zrx4w.jpg'
        )
        artist3 = Artist(
            name='Bon Jovi',
            gender='Male',
            age=61,
            birth_date=datetime.strptime('1962-03-02', '%Y-%m-%d'),
            birth_place='Perth Amboy, New Jersey',
            biography='Bon Jovi is an American rock band formed in 1983.',
            image='https://facts.net/wp-content/uploads/2023/07/14-facts-about-bon-jovi-1689324847.jpg'
        )
        artist4 = Artist(
            name='Bad Bunny',
            gender='Male',
            age=30,
            birth_date=datetime.strptime('1994-03-10', '%Y-%m-%d'),
            birth_place='San Juan, Puerto Rico',
            biography='Bad Bunny is a Puerto Rican singer, rapper, and songwriter.',
            image='https://th.bing.com/th/id/OIP.NLc_2QNJ6df50qdpDYNncgHaEK?rs=1&pid=ImgDetMain'
        )
        artist5 = Artist(
            name='Kendrick Lamar',
            gender='Male',
            age=37,
            birth_date=datetime.strptime('1987-06-17', '%Y-%m-%d'),
            birth_place='Compton, California',
            biography='Kendrick Lamar is an American rapper, songwriter, and record producer.',
            image='https://i.pinimg.com/originals/49/f7/83/49f7839f13bcf6f698ecda00c3077372.jpg'
        )
        artist6 = Artist(
            name='Beyoncé',
            gender='Female',
            age=42,
            birth_date=datetime.strptime('1981-09-04', '%Y-%m-%d'),
            birth_place='Houston, Texas, USA',
            biography='Beyoncé is an American singer, songwriter, and actress, and one of the best-selling music artists of all time.',
            image='https://www.wallpics.net/wp-content/uploads/2018/01/Beyonce-Knowles-HD.jpg'
        )
        artist7 = Artist(
            name='Rihanna',
            gender='Female',
            age=36,
            birth_date=datetime.strptime('1988-02-20', '%Y-%m-%d'),
            birth_place='Saint Michael, Barbados',
            biography='Rihanna is a Barbadian singer, actress, and businesswoman. She is known for her distinctive voice and diverse musical style.',
            image='https://support.musicgateway.com/wp-content/uploads/2022/12/Rhianna.jpg'
        )
        artist8 = Artist(
            name='Ella Mai',
            gender='Female',
            age=29,
            birth_date=datetime.strptime('1994-11-03', '%Y-%m-%d'),
            birth_place='London, England, UK',
            biography='Ella Mai is a British singer-songwriter known for her hit single "Boo’d Up" and her contemporary R&B sound.',
            image='https://imgix.ranker.com/list_img_v2/216/3160216/original/3160216'
        )
        artist9 = Artist(
            name='Taylor Swift',
            gender='Female',
            age=34,
            birth_date=datetime.strptime('1989-12-13', '%Y-%m-%d'),
            birth_place='Reading, Pennsylvania, USA',
            biography='Taylor Swift is an American singer-songwriter known for her narrative songwriting and successful career across multiple music genres.',
            image='https://th.bing.com/th/id/OIP.7Vm85cfxiV9HsLb7E3bMMgHaJJ?rs=1&pid=ImgDetMain'
        )
        artist10 = Artist(
            name='Jay-Z',
            gender='Male',
            age=54,
            birth_date=datetime.strptime('1969-12-04', '%Y-%m-%d'),
            birth_place='Brooklyn, New York, USA',
            biography='Jay-Z is an American rapper, songwriter, record executive, and businessman. He is regarded as one of the greatest rappers of all time.',
            image='https://th.bing.com/th/id/OIP.SuTOA4oFll1xL18aCYWiJQHaE8?rs=1&pid=ImgDetMain'
        )
        
        db.session.bulk_save_objects([artist1, artist2, artist3, artist4, artist5, artist6, artist7, artist8, artist9, artist10])
        db.session.commit()
        
        artist_ids = {artist.name: artist.id for artist in Artist.query.all()}
        return artist_ids

def create_songs(artist_ids):
    with app.app_context():
        song1 = Song(
            name='Stronger',
            genre='Hip-Hop',
            length=305,
            lyrics='That that don’t kill me can only make me stronger',
            release_dt=datetime.strptime('2007-09-11', '%Y-%m-%d'),
            image='https://upload.wikimedia.org/wikipedia/en/d/d7/KW-Stronger.jpg',
            artist_id=artist_ids['Kanye West']
        )
        song2 = Song(
            name='Uptown Funk',
            genre='Pop',
            length=269,
            lyrics='Don’t believe me, just watch',
            release_dt=datetime.strptime('2014-11-10', '%Y-%m-%d'),
            image='https://th.bing.com/th/id/OIP.67bxlko6Hc-JdgDEFP5RaQHaE8?rs=1&pid=ImgDetMain',
            artist_id=artist_ids['Bruno Mars']
        )
        song3 = Song(
            name='Livin’ on a Prayer',
            genre='Rock',
            length=240,
            lyrics='Woah, we’re halfway there',
            release_dt=datetime.strptime('1986-10-31', '%Y-%m-%d'),
            image='https://m.media-amazon.com/images/M/MV5BMjE0ZTVlZTktZjY3My00NDhiLThjZjMtMDlmOGVlNjY0ZjAzXkEyXkFqcGdeQXVyNDQ5MDYzMTk@._V1_.jpg',
            artist_id=artist_ids['Bon Jovi']
        )
        song4 = Song(
            name='Safaera',
            genre='Reggaeton',
            length=230,
            lyrics='Baby, yo no quiero na’',
            release_dt=datetime.strptime('2020-02-28', '%Y-%m-%d'),
            image='https://media.pitchfork.com/photos/5e5d895d19382e0008724f89/1:1/w_800,h_800,c_limit/YHLQMDLG_Bad%20Bunny.jpg',
            artist_id=artist_ids['Bad Bunny']
        )
        song5 = Song(
            name='No Rest for the Wicked',
            genre='Regional Mexican',
            length=215,
            lyrics='Ya me voy a ir',
            release_dt=datetime.strptime('2022-04-15', '%Y-%m-%d'),
            image='https://upload.wikimedia.org/wikipedia/en/a/ad/Ain%27t_no_rest_for_the_wicked.jpg',
            artist_id=artist_ids['Kendrick Lamar']
        )
        song6 = Song(
            name='HUMBLE.',
            genre='Hip-Hop',
            length=177,
            lyrics='I’m so fuckin’ sick and tired of the Photoshop',
            release_dt=datetime.strptime('2017-03-30', '%Y-%m-%d'),
            image='https://m.media-amazon.com/images/M/MV5BOTUwNzRiNDAtN2E2ZC00ZTk1LWE1OGYtZGU3YjliYTA0NjdhXkEyXkFqcGc@._V1_.jpg',
            artist_id=artist_ids['Kendrick Lamar']
        )
        song7 = Song(
            name='Halo',
            genre='Pop',
            length=261,
            lyrics='Remember those walls I built, well baby they’re tumbling down...',
            release_dt=datetime.strptime('2008-01-20', '%Y-%m-%d'),
            image='https://upload.wikimedia.org/wikipedia/en/4/4e/Beyonce_Halo.png',
            artist_id=artist_ids['Beyoncé']
        )
        song8 = Song(
            name='Diamonds',
            genre='Pop',
            length=243,
            lyrics='Shine bright like a diamond',
            release_dt=datetime.strptime('2012-11-19', '%Y-%m-%d'),
            image='https://m.media-amazon.com/images/I/71xi0hKt4sL._SS500_.jpg',
            artist_id=artist_ids['Rihanna']
        )
        song9 = Song(
            name='Boo’d Up',
            genre='R&B',
            length=238,
            lyrics='Love, when you love somebody...',
            release_dt=datetime.strptime('2018-05-04', '%Y-%m-%d'),
            image='https://i.scdn.co/image/ab67616d0000b2730923cf5e54f6d46e4e0176f7',
            artist_id=artist_ids['Ella Mai']
        )
        song10 = Song(
            name='Blank Space',
            genre='Pop',
            length=231,
            lyrics='Got a long list of ex-lovers',
            release_dt=datetime.strptime('2014-11-10', '%Y-%m-%d'),
            image='https://upload.wikimedia.org/wikipedia/en/2/22/Blank_Space.png',
            artist_id=artist_ids['Taylor Swift']
        )
        song11 = Song(
            name='99 Problems',
            genre='Hip-Hop',
            length=220,
            lyrics='If you’re havin’ girl problems I feel bad for you, son...',
            release_dt=datetime.strptime('2003-06-16', '%Y-%m-%d'),
            image='https://upload.wikimedia.org/wikipedia/en/2/27/Jay-Z_-_99_Problems.jpg',
            artist_id=artist_ids['Jay-Z']
        )

        db.session.bulk_save_objects([song1, song2, song3, song4, song5, song6, song7, song8, song9, song10, song11])
        db.session.commit()

if __name__ == '__main__':
    artist_ids = create_artists()
    create_songs(artist_ids)


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

# if __name__ == '__main__':
#     # create_users()
#     create_songs()
#     create_artists()
