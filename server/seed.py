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
            image='https://i.pinimg.com/736x/f3/5c/59/f35c5921869b22f39ea9f8a1b5a9b04b.jpg',
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
            image='data:image/jpeg;base64,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',
            artist_id=artist_ids['Beyoncé']
        )
        song8 = Song(
            name='Diamonds',
            genre='Pop',
            length=243,
            lyrics='Shine bright like a diamond',
            release_dt=datetime.strptime('2012-11-19', '%Y-%m-%d'),
            image='data:image/jpeg;base64,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',
            artist_id=artist_ids['Rihanna']
        )
        song9 = Song(
            name='Boo’d Up',
            genre='R&B',
            length=238,
            lyrics='Love, when you love somebody...',
            release_dt=datetime.strptime('2018-05-04', '%Y-%m-%d'),
            image='https://images.genius.com/14e6b95f30822290e1dd0a7779272243.1000x1000x1.jpg',
            artist_id=artist_ids['Ella Mai']
        )
        song10 = Song(
            name='Love Story',
            genre='Pop',
            length=231,
            lyrics='Got a long list of ex-lovers',
            release_dt=datetime.strptime('2014-11-10', '%Y-%m-%d'),
            image='data:image/jpeg;base64,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',
            artist_id=artist_ids['Taylor Swift']
        )
        song11 = Song(
            name='99 Problems',
            genre='Hip-Hop',
            length=220,
            lyrics='If you’re havin’ girl problems I feel bad for you, son...',
            release_dt=datetime.strptime('2003-06-16', '%Y-%m-%d'),
            image='data:image/jpeg;base64,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',
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