""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash


'''Class Setup '''

    # Defining the NFLNews class to manage actions in the 'news' table

class NFLTeam(db.Model):
    __tablename__ = 'NFLNews'  

    # Defining the Object Variable

    id = db.Column(db.Integer, primary_key=True)
    _team = db.Column(db.String(255), unique=False, nullable=False)
    _playoffs = db.Column(db.String(255), unique=False, nullable=False)
    _gamesplayed = db.Column(db.Integer, primary_key=True)
    _gameswon = db.Column(db.Integer, primary_key=True)
    _gameslost = db.Column(db.Integer, primary_key=True)
    _gamesdrawn = db.Column(db.Integer, primary_key=True)
    _gamesplayedathome = db.Column(db.Integer, primary_key=True)
    _gamesplayedaway = db.Column(db.Integer, primary_key=True)
    _gameswonathome = db.Column(db.Integer, primary_key=True)
    _gameslostathome = db.Column(db.Integer, primary_key=True)
    _gameswonaway = db.Column(db.Integer, primary_key=True)
    _gameslostaway = db.Column(db.Integer, primary_key=True)
    _gamesplayed5 = db.Column(db.Integer, primary_key=True)
    _gameswon5 = db.Column(db.Integer, primary_key=True)
    _gameslost5 = db.Column(db.Integer, primary_key=True)
    _pointsfor = db.Column(db.Integer, primary_key=True)
    _pointsagainst = db.Column(db.Integer, primary_key=True)
    _pointsinfourthquarter = db.Column(db.Integer, primary_key=True)
    _pctoverall = db.Column(db.Integer, primary_key=True)
    _pcthome = db.Column(db.Integer, primary_key=True)
    _pctaway = db.Column(db.Integer, primary_key=True)
    _pctlast5 = db.Column(db.Integer, primary_key=True)
    
    

    # Constructor of a NFLTeam object, initializes the instance variables within object (self)

    def __init__(self, team, gamesplayed, gameswon, gameslost, gamesdrawn, gamesplayedathome, gamesplayedaway, gameswonathome, gameslostathome, gameswonaway, gameslostaway, gamesplayed5, gameswon5, gameslost5, pointsfor, pointsagainst, pointsinfourthquarter, playoffs):

        self._team = team    # variables with "own"" prefix become part of the object
        self._gamesplayed = gamesplayed
        self._gameswon = gameswon
        self._gameslost = gameslost
        self._gamesdrawn = gamesdrawn
        self. _gamesplayedathome = gamesplayedathome
        self._gamesplayedaway = gamesplayedaway
        self._gameswonathome = gameswonathome
        self._gameslostathome = gameslostathome
        self._gameswonaway = gameswonaway
        self. _gameslostaway = gameslostaway
        self._gamesplayed5 = gamesplayed5
        self._gameswon5 = gameswon5
        self._gameslost5 = gameslost5
        self._pointsfor = pointsfor
        self._pointsagainst = pointsagainst
        self._pointsinfourthquarter = pointsinfourthquarter
        self._playoffs = playoffs

  
    """Setter and Getter Methods for all Variables"""  

    @property
    def team(self):
        return self._team
    
    @team.setter
    def team(self, team):
        self._team = team
    
    @property
    def gamesplayed(self):
        return self._gamesplayed
    
    @gamesplayed.setter
    def gamesplayed(self, gamesplayed):
        self._gamesplayed = gamesplayed

    @property
    def gameswon(self):
        return self._gameswon
    
    @gameswon.setter
    def gameswon(self, gameswon):
        self._gameswon = gameswon

    @property
    def gameslost(self):
        return self._gameslost
    
    @gameslost.setter  
    def gameslost(self, gameslost):
       self._gameslost = gameslost

    @property
    def gamesdrawn(self):
        return self._gamesdrawn
    
    @gamesdrawn.setter  
    def gamesdrawn(self, gamesdrawn):
       self._gamesdrawn = gamesdrawn

    @property
    def gamesplayedathome(self):
        return self._gamesplayedathome
    
    @gamesplayedathome.setter
    def gamesplayedathome(self, gamesplayedathome):
       self._gamesplayedathome = gamesplayedathome

    @property
    def gamesplayedaway(self):
        return self._gamesplayedaway
    
    @gamesplayedaway.setter
    def gamesplayedaway(self, gamesplayedaway):
       self._gamesplayedaway = gamesplayedaway

    @property
    def gameswonathome(self):
        return self._gameswonathome
    
    @gameswonathome.setter
    def gameswonathome(self, gameswonathome):
       self._gameswonathome = gameswonathome

    @property
    def gameslostathome(self):
        return self._gameslostathome
    
    @gameslostathome.setter
    def gameslostathome(self, gameslostathome):
       self._gameslostathome = gameslostathome

    @property
    def gameswonaway(self):
        return self._gameswonaway
    
    @gameswonaway.setter
    def gameswonaway(self, gameswonaway):
       self._gameswonaway = gameswonaway

    @property
    def gameslostaway(self):
        return self._gameslostaway
    
    @gameslostaway.setter
    def  gameslostaway(self, gameslostaway):
       self._gameslostaway = gameslostaway

    @property
    def gamesplayed5(self):
        return self._gamesplayed5
    
    @gamesplayed5.setter
    def  gamesplayed5(self, gamesplayed5):
       self._gamesplayed5 = gamesplayed5

    @property
    def gameswon5(self):
        return self._gameswon5
    
    @gameswon5.setter
    def gameswon5(self, gameswon5):
       self._gameswon5 = gameswon5

    @property
    def gameslost5(self):
        return self._gameslost5
    
    @gameslost5.setter
    def gameslost5(self, gameslost5):
       self._gameslost5 = gameslost5

    @property
    def pointsfor(self):
        return self._pointsfor
    
    @pointsfor.setter
    def pointsfor(self, pointsfor):
       self._pointsfor = pointsfor
   
    @property
    def pointsagainst(self):
        return self._pointsagainst
    
    @pointsagainst.setter
    def pointsagainst(self, pointsagainst):
       self._pointsagainst = pointsagainst

    @property
    def pointsinfourthquarter(self):
        return self._pointsinfourthquarter
    
    @pointsinfourthquarter.setter
    def pointsinfourthquarter(self, pointsinfourthquarter):
       self._pointsinfourthquarter = pointsinfourthquarter


    def __str__(self):
        return json.dumps(self.read())


    """CRUD METHODS """  
    def create(self):
        try:
            # creates a NFL News object from NFLNews(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist NFL News object to NFLNews table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


    def read(self):
        return {
            "team": self.team,
            "gamesplayed": self._gamesplayed,
            "gameswon": self.gameswon,
            "gameslost": self.gameslost
            
        }



"""Database Creation and Testing """

# Builds working data for testing

def initNFLNews():
    print("Creating test data")
    """Create database and tables"""
    db.create_all()
    """Tester data for table"""

    
    t3 = NFLTeam(team = "Washington Commanders", gamesplayed = 17, gameswon = 8, gameslost = 8, gamesdrawn = 1, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=4, gameslostathome=5, gameswonaway=4, gameslostaway=3, gamesplayed5=5, gameswon5=2, gameslost5=3, pointsfor=321, pointsagainst=343)
    t3 = NFLTeam(team = "New York Giants", gamesplayed = 17, gameswon = 8, gameslost = 8, gamesdrawn = 1, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=4, gameslostathome=5, gameswonaway=4, gameslostaway=3, gamesplayed5=5, gameswon5=2, gameslost5=3, pointsfor=321, pointsagainst=343)

    t1 = NFLTeam(team = "Arizona Cradinals", gamesplayed = 17, gameswon = 4, gameslost = 13, gamesdrawn = 0, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=1, gameslostathome=8, gameswonaway=3, gameslostaway=5, gamesplayed5=5, gameswon5=0, gameslost5=5, pointsfor=340, pointsagainst=449, pointsinfourthquarter=70)
    t2 = NFLTeam(team = "Los Angeless Rams", gamesplayed = 17, gameswon = 5, gameslost = 12, gamesdrawn = 0, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=4, gameslostathome=5, gameswonaway=1, gameslostaway=7, gamesplayed5=5, gameswon5=3, gameslost5=2, pointsfor=307, pointsagainst=384, pointsinfourthquarter=84)
    t3 = NFLTeam(team = "Washington Commanders", gamesplayed = 17, gameswon = 8, gameslost = 8, gamesdrawn = 1, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=1, gameslostathome=9, gameswonaway=3, gameslostaway=5, gamesplayed5=5, gameswon5=2, gameslost5=3, pointsfor=321, pointsagainst=343, pointsinfourthquarter=74)
    
    t4 = NFLTeam(team = "New England Patriots", gamesplayed = 17, gameswon = 8, gameslost = 9, gamesdrawn = 0, gamesplayedathome=8, gamesplayedaway=9, gameswonathome=4, gameslostathome=4, gameswonaway=4, gameslostaway=5, gamesplayed5=5, gameswon5=0, gameslost5=5, pointsfor=296, pointsagainst=316, pointsinfourthquarter= 62)
    t5 = NFLTeam(team = "Houston Texans", gamesplayed = 17, gameswon = 3, gameslost = 13, gamesdrawn = 1, gamesplayedathome=7, gamesplayedaway=9, gameswonathome=0, gameslostathome=7, gameswonaway=3, gameslostaway=6, gamesplayed5=5, gameswon5=0, gameslost5=5, pointsfor=340, pointsagainst=449, pointsinfourthquarter=70)
    t5 = NFLTeam(team = "Kansas City Chiefs", gamesplayed = 17, gameswon = 4, gameslost = 13, gamesdrawn = 0, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=4, gameslostathome=5, gameswonaway=4, gameslostaway=3, gamesplayed5=5, gameswon5=1, gameslost5=5, pointsfor=289, pointsagainst=420, pointsinfourthquarter=42)
    
    t6 = NFLTeam(team = "Green Bay Packers", gamesplayed = 17, gameswon = 8, gameslost = 9, gamesdrawn = 0, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=5, gameslostathome=4, gameswonaway=3, gameslostaway=5, gamesplayed5=5, gameswon5=3, gameslost5=2, pointsfor=370, pointsagainst=371, pointsinfourthquarter=106)
    t7 = NFLTeam(team = "Chicago Bears", gamesplayed = 17, gameswon = 3, gameslost = 14, gamesdrawn = 0, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=2, gameslostathome=7, gameswonaway=1, gameslostaway=7, gamesplayed5=5, gameswon5=0, gameslost5=5, pointsfor=326, pointsagainst=463, pointsinfourthquarter=81)
    t8 = NFLTeam(team = "Atlanta Falcons", gamesplayed = 17, gameswon = 7, gameslost = 10, gamesdrawn = 0, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=4, gameslostathome=5, gameswonaway=3, gameslostaway=5, gamesplayed5=5, gameswon5=3, gameslost5=2, pointsfor=330, pointsagainst=345, pointsinfourthquarter=79)
    t9 = NFLTeam(team = "New Orleans Saints", gamesplayed = 17, gameswon = 7, gameslost = 10, gamesdrawn = 0, gamesplayedathome=9, gamesplayedaway=8, gameswonathome=6, gameslostathome=3, gameswonaway=1, gameslostaway=7, gamesplayed5=5, gameswon5=2, gameslost5=3, pointsfor=365, pointsagainst=386, pointsinfourthquarter=65)

    t10 = NFLTeam(team = "Indeanappolis Colts", gamesplayed = 17, gameswon = 4, gameslost = 12, gamesdrawn = 0, gamesplayedathome=8, gamesplayedaway=9, gameswonathome=2, gameslostathome=6, gameswonaway=2, gameslostaway=6, gamesplayed5=5, gameswon5=2, gameslost5=3, pointsfor=289, pointsagainst=427, pointsinfourthquarter=54)

    """Builds sample user/note(s) data"""
    for news in nfl_news:
        try:
            news.create()
        except IntegrityError:
            '''fails with bad or duplicate data'''
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {news.uid}")
