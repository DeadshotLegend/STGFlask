""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash


''' Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along '''

    # Defining the NFLNews class to manage actions in the 'news' table

class NFLNews(db.Model):
    __tablename__ = 'NFLNews'  

    # Defining the Object Variable


    _teams = db.Column(db.String(255), unique=False, nullable=False)
    _score = db.Column(db.String(255), unique=False, nullable=False)
    _type = db.Column(db.String(255), unique=False, nullable=False)
    _day = db.Column(db.Date)

    # Constructor of a User object, initializes the instance variables within object (self)

    def __init__(own, teams, score, type, day=date.today()):

        own._teams = teams    # variables with "own"" prefix become part of the object
        own._score = score
        own._type = type
        own._day = day

    # Getter and setter methods for all variables

    @property
    def teams(own):
        return own._teams
    
    @teams.setter
    def teams(own, teams):
        own._teams = teams
    
    @property
    def score(own):
        return own._score
    
    @score.setter
    def score(own, score):
        own.score = score


    @property
    def type(own):
        return own.type
    
    @type.setter
    def score(own, type):
        own.type = type

      
    @property
    def day(own):
        day_string = own._day.strftime('%m-%d-%Y')
        return day_string
    

    @day.setter
    def day(own, day):
        own._day = day
    
    
    
  
    def __str__(own):
        return json.dumps(own.read())

    
    def create(own):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(own)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return own
        except IntegrityError:
            db.session.remove()
            return None


    def read(own):
        return {

            "teams": own.teams,
            "score": own.score,
            "type": own.type,
            "day": own.day
            
        }
    
    def delete(own):
        db.session.delete(own)
        db.session.commit()
        return None


"""Database Creation and Testing """

# Builds working data for testing

def initNFLNews():
    """Create database and tables"""
    db.create_all()
    """Tester data for table"""
    u1 = NFLNews(teams = 'Bufallo Bils vs Cincanatti Bengals', score='10:27', type = 'Divisonal Round', day=date(2023, 1, 22))

    
    nfl_news = [u1]


    """Builds sample user/note(s) data"""
    for news in nfl_news:
        try:
            news.create()
        except IntegrityError:
            '''fails with bad or duplicate data'''
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {news.uid}")