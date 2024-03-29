from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.nflnews import NFLNews

nflnews_api = Blueprint('nflnews_api', __name__,
                   url_prefix='/api/nflnews')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(nflnews_api)

class NFLNewsAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            team = body.get('teams')
            if team is None or len(team) < 2:
                return {'message': f'Team is missing, or is less than 2 characters'}, 210
            
            # look for score, type
            score = body.get('score')
            type = body.get('type')
            #day = body.get('day')
            # validate uid
            #uid = body.get('id')
            #if uid is None or len(uid) < 2:
            #    return {'message': f'ID is missing, or is less than 2 characters'}, 210
            #''' #1: Key code block, setup USER OBJECT '''
            
            uo = NFLNews(teams=team, score=score, type=type)
            
            ''' Additional garbage error checking '''
            
            # create nfl news in database
            nflnews = uo.create()
            # success returns json of nfl news
            if nflnews:
                return jsonify(nflnews.read())
            # failure returns error
            return {'message': f'Processed news error'}, 210

    class _Read(Resource):
        def get(self):
            newitems = NFLNews.query.all()    # read/extract all users from database
            json_ready = [newitem.read() for newitem in newitems]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')