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

    id = db.Column(db.Integer, primary_key=True)
    _team = db.Column(db.String(255), unique=False, nullable=False)
    _gamesplayed = db.Column(db.Integer, primary_key=True)
    _gameswon = db.Column(db.Integer, primary_key=True)
    _gameslost = db.Column(db.Integer, primary_key=True)

    # Constructor of a NFLNews object, initializes the instance variables within object (self)

    def __init__(self, teams, score, type, day=date.today()):

        self._teams = teams    # variables with "own"" prefix become part of the object
        self._score = score
        self._type = type
        self._day = day

    # Getter and setter methods for all variables

    @property
    def teams(self):
        return self._teams
    
    @teams.setter
    def teams(self, teams):
        self._teams = teams
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score


    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        self._type = type

      
    @property
    def day(self):
        day_string = self._day.strftime('%m-%d-%Y')
        return day_string
    

    @day.setter
    def day(self, day):
        self._day = day
    
    
    
  
    def __str__(self):
        return json.dumps(self.read())

    
    def create(self):
        try:
            # creates a NFL News object from NFLNews(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist NFL News object to NFLNews table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None


    def read(self):
        return {
            "id": self.id,
            "teams": self.teams,
            "score": self.score,
            "type": self.type,
            "day": self.day
            
        }
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing """

# Builds working data for testing

def initNFLNews():
    print("Creating test data")
    """Create database and tables"""
    db.create_all()
    """Tester data for table"""
    u1 = NFLNews(teams = 'Bufallo Bils vs Cincanatti Bengals', score='10:27', type = 'Divisonal Round', day=date(2023, 1, 22))
    u2 = NFLNews(teams = 'Dallas Cowboys vs San Francisco 49ers', score='12:19', type = 'Divisonal Round', day=date(2023, 1, 22))
    u3 = NFLNews(teams = 'New York Giants vs Philadelphia Eagles', score='7:37', type = 'Divisonal Round', day=date(2023, 1, 22))
    u4 = NFLNews(teams = 'Jacksonville Jaguars vs Kansas City Cheifs', score='20:27', type = 'Divisonal Round', day=date(2023, 1, 22))
    u5 = NFLNews(teams = 'Dallas Cowboys vs Tampa Bay Buccanears', score='31:14', type = 'Wildcard Round', day=date(2023, 1, 22))
    u6 = NFLNews(teams = 'Baltimore Ravens vs Cincanatti Bengals', score='17:24', type = 'Wildcard Round', day=date(2023, 1, 22))

    
    nfl_news = [u1, u2, u3, u4, u5, u6]


    """Builds sample user/note(s) data"""
    for news in nfl_news:
        try:
            news.create()
        except IntegrityError:
            '''fails with bad or duplicate data'''
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {news.uid}")
