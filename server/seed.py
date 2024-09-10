#!/usr/bin/env python3

# Standard library imports
from datetime import datetime
import csv

# Local imports
from app import app
from models import db, Artist, Song, Review, Favorite, User

def clear_database():
    """Clear all data from the database."""
    with app.app_context():
        Artist.query.delete()
        Song.query.delete()
        Review.query.delete()
        Favorite.query.delete()
        User.query.delete()
        db.session.commit()

def create_artists(rows):
    """Seed artists into the database."""
    with app.app_context():
        artists = []
        for i in range(1, len(rows)):
            try:
                artist = Artist(
                    name=rows[i][1],  # Name should be at index 1
                    age=int(rows[i][2]),  # Age should be at index 2
                    gender=rows[i][3],  # Gender at index 3
                    birth_date=datetime.strptime(rows[i][0], '%Y-%m-%d'),  # Birth date at index 0
                    birth_place=rows[i][4],
                    biography=rows[i][5],
                    image=rows[i][6]
                )
                artists.append(artist)
            except ValueError as ve:
                print(f"Error creating artist: {ve}")  # Capture the specific value error
            except Exception as e:
                print(f"General error creating artist: {e}")
        db.session.add_all(artists)
        db.session.commit()
    return artists

def create_songs(rows):
    """Seed songs into the database."""
    with app.app_context():
        songs = []
        for i in range(1, len(rows)):
            try:
                song = Song(
                    name=rows[i][7],  # Song name at index 7
                    length=int(rows[i][8]),  # Song length at index 8
                    genre=rows[i][9],  # Song genre at index 9
                    lyrics=rows[i][10],  # Song lyrics at index 10
                    release_dt=datetime.strptime(rows[i][11], '%Y-%m-%d'),  # Song release date at index 11
                    image=rows[i][12]  # Song image at index 12
                )
                songs.append(song)
            except Exception as e:
                print(f"Error creating song: {e}")
        db.session.add_all(songs)
        db.session.commit()
    return songs

def create_users(rows):
    """Seed users into the database."""
    with app.app_context():
        users = []
        for i in range(1, len(rows)):
            try:
                user = User(
                    username=rows[i][13],  # Username at index 13
                    email=rows[i][14],  # Email at index 14
                    password=rows[i][15]  # Password at index 15
                )
                users.append(user)
            except Exception as e:
                print(f"Error creating user: {e}")
        db.session.add_all(users)
        db.session.commit()
    return users

def create_favorites(rows, users, artists):
    """Seed favorites into the database."""
    with app.app_context():
        favorites = []
        for i in range(1, len(rows)):
            try:
                user = User.query.filter_by(username=rows[i][13]).first()  # Username at index 13
                artist = Artist.query.filter_by(name=rows[i][19]).first()  # Favorite name at index 19
                if user and artist:
                    favorite = Favorite(user=user, artist=artist)
                    favorites.append(favorite)
            except Exception as e:
                print(f"Error creating favorite: {e}")
        db.session.add_all(favorites)
        db.session.commit()  # Ensure to commit the favorites to the session
    return favorites

def create_reviews(rows, artists, songs, users):
    """Seed reviews into the database."""
    with app.app_context():
        reviews = []
        for i in range(1, len(rows)):
            try:
                artist = Artist.query.filter_by(name=rows[i][1]).first()  # Artist name at index 1
                song = Song.query.filter_by(name=rows[i][7]).first()  # Song name at index 7
                user = User.query.filter_by(username=rows[i][13]).first()  # Username at index 13
                if artist and song and user:
                    review = Review(
                        rating=int(rows[i][16]),  # Rating at index 16
                        comment=rows[i][17],  # Comment at index 17
                        artist=artist,
                        song=song,
                        user=user
                    )
                    reviews.append(review)
            except Exception as e:
                print(f"Error creating review: {e}")
        db.session.add_all(reviews)
        db.session.commit()  # Ensure reviews are committed
    return reviews


if __name__ == '__main__':
    print("Clearing database...")
    clear_database()

    try:
        print("Opening CSV...")
        with open('seed.csv', newline='') as csvfile:
            rows = [row for row in csv.reader(csvfile, delimiter=',', quotechar='|')]
            
            print("Seeding artists...")
            artists = create_artists(rows)
            
            print("Seeding songs...")
            songs = create_songs(rows)
            
            print("Seeding users...")
            users = create_users(rows)
            
            print("Seeding favorites...")
            favorites = create_favorites(rows, users, artists)
            
            print("Seeding reviews...")
            create_reviews(rows, artists, songs, users)
            
            print("Seeding complete!")
    except FileNotFoundError:
        print("Error: CSV file not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
