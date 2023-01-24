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
    __tablename__ = 'NFL News'  

    # Defining the User Constructor

    id = db.Column(db.Integer, primary_key=True)
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
        return own._
    
    @score.setter
    def score(own, score):
        own.score = score
        

    def is_score(own, score):
        return own._score == score
      
    @property
    def day(own):
        day_string = own._day.strftime('%m-%d-%Y')
        return day_string
    

    @day.setter
    def day(own, day):
        own._day = day
    
    @property
    def age(own):
        today = date.today()
        return today.year - own._day.year - ((today.month, today.day) < (own._day.month, own._day.day))
    
    # output content using str(object) in human readable form, uses getter
    # output content using json dumps, this is ready for API response
    def __str__(own):
        return json.dumps(own.read())

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(own):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(own)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return own
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(own):
        return {

            "teams": own.teams,
            "score": own.score,
            "age": own.age,
            "day": own.day
            
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(own, teams="", score=""):
        """only updates values with length"""
        if len(teams) > 0:
            own.teams = teams
        if len(score) > 0:
            own.score = score
        db.session.commit()
        return own

    # CRUD delete: remove self
    # None
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
    u1 = NFLNews(title='Bolsonaro supporters storm Brazilian Congress.', network='CNN', day=date(2023, 1, 21))
    u2 = NFLNews(title='Kevin McCarthy is new speaker', network='Fox', day=date(2023, 1, 20))
    u3 = NFLNews(title='Woman sentenced to three years in state prison for collecting 400,000 in viral GoFundMe scam', network='ABC', day=date(2023, 1, 19))
    u4 = NFLNews(title='Ukraine denies Russian claim it killed 600 soldiers', network='NBC', day=date(2023, 1, 20))
    u5 = NFLNews(title='Damar Hamlin: Buffalo Bills make stirring display in support of safety during victory', network='BBC', day=date(2023, 1, 22))
    u6 = NFLNews(title='Worshippers in Tokyo plunge into ice bath to mark new year', network='CNN', day=date(2023, 1, 21))
    u7 = NFLNews(title='Driver crashes and flips vehicle inside drive-through car wash', network='Fox', day=date(2023, 1, 20))
    u8 = NFLNews(title='Brazilian police fire tear gas at Bolsonaro supporters', network='ABC', day=date(2023, 1, 19))
    u9 = NFLNews(title='Deer rescued from frozen river in Wisconsin', network='NBC', day=date(2023, 1, 20))
    u10 = NFLNews(title='Two years after Covid food still tastes rotten', network='BBC', day=date(2023, 1, 22))

    
    nfl_news = [u1, u2, u3, u4, u5, u6, u7, u8, u9, u10]
    # breaking_news = [u1, u2, u3, u4, u5]

    """Builds sample user/note(s) data"""
    for news in nfl_news:
        try:
            news.create()
        except IntegrityError:
            '''fails with bad or duplicate data'''
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {news.uid}")