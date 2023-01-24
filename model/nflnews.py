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
    _score = db.Column(db.Integer, primary_key=True)
    _record = db.Column(db.String(255), unique=False, nullable=False)

    # Constructor of a User object, initializes the instance variables within object (self)

    def __init__(teams, score, network, day=date.today()):
        self._teams = title    # variables with self prefix become part of the object, 
        self._network = network
        self._day = day

    # a name getter method, extracts name from object
    @property
    def title(self):
        return self._teams
    
    # a setter function, allows name to be updated after initial object creation
    @title.setter
    def title(self, title):
        self._teams = title
    
    # a getter method, extracts email from object
    @property
    def network(self):
        return self._network
    
    # a setter function, allows name to be updated after initial object creation
    @network.setter
    def network(self, network):
        self._network = network
        
    # check if uid parameter matches user id in object, return boolean
    def is_network(self, network):
        return self._network == network
      
    # dob property is returned as string, to avoid unfriendly outcomes
    @property
    def day(self):
        day_string = self._day.strftime('%m-%d-%Y')
        return day_string
    
    # dob should be have verification for type date
    @day.setter
    def day(self, day):
        self._day = day
    
    @property
    def age(self):
        today = date.today()
        return today.year - self._day.year - ((today.month, today.day) < (self._day.month, self._day.day))
    
    # output content using str(object) in human readable form, uses getter
    # output content using json dumps, this is ready for API response
    def __str__(self):
        return json.dumps(self.read())

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "id": self.id,
            "title": self.title,
            "network": self.network,
            "day": self.day,
            "age": self.age
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, title="", network=""):
        """only updates values with length"""
        if len(title) > 0:
            self.title = title
        if len(network) > 0:
            self.network = network
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
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