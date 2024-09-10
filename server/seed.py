#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Artist, Song, Review, Favorite, User
import csv

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
                artist = Artist(date=rows[i][2], number=i)
                artists.append(artist)
            except Exception as e:
                print(f"Error creating artist: {e}")
        db.session.add_all(artists)
        db.session.commit()
    return artists

def create_songs(rows):
    """Seed songs into the database."""
    with app.app_context():
        songs = []
        for i in range(1, len(rows)):
            try:
                song = Song(name=rows[i][-1], occupation=rows[i][1])
                songs.append(song)
            except Exception as e:
                print(f"Error creating song: {e}")
        db.session.add_all(songs)
        db.session.commit()
    return songs

def create_reviews(rows, artists, songs, favorites, users):
    """Seed reviews into the database."""
    with app.app_context():
        reviews = []
        for i in range(1, len(rows)):
            try:
                review = Review(
                    rating=randint(1, 5),
                    song=Song.query.filter_by(name=rows[i][-1]).first(),
                    # artist=Artist.query.filter_by(date=rows[i][2]).first(),
                    # favorite=Favorite.query.filter_by(name=rows[i][3]).first(),
                    # user=User.query.filter_by(name=rows[i][4]).first()
                )
                reviews.append(review)
            except Exception as e:
                print(f"Error creating review: {e}")
        db.session.add_all(reviews)
        db.session.commit()
    return reviews

def create_favorites(rows):
    """Seed favorites into the database."""
    with app.app_context():
        favorites = []
        for i in range(1, len(rows)):
            try:
                favorite = Favorite(name=rows[i][-1], occupation=rows[i][1])
                favorites.append(favorite)
            except Exception as e:
                print(f"Error creating favorite: {e}")
        db.session.add_all(favorites)
        db.session.commit()
    return favorites

def create_users(rows):
    """Seed users into the database."""
    with app.app_context():
        users = []
        for i in range(1, len(rows)):
            try:
                user = User(name=rows[i][-1], occupation=rows[i][1])
                users.append(user)
            except Exception as e:
                print(f"Error creating user: {e}")
        db.session.add_all(users)
        db.session.commit()
    return users

if __name__ == '__main__':
    fake = Faker()
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
            print("Seeding favorites...")
            favorites = create_favorites(rows)
            print("Seeding users...")
            users = create_users(rows)
            print("Seeding reviews...")
            create_reviews(rows, artists, songs, favorites, users)
            print("Complete!")
    except FileNotFoundError:
        print("Error: CSV file not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


    