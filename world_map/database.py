from pymongo import MongoClient
from os import environ

try:
    _people = MongoClient(
        f'mongodb://{environ["MONGODB_USER"]}:{environ["MONGODB_PASSWORD"]}@{environ.get("MONGODB_HOST", "localhost")}/{environ["MONGODB_DATABASE"]}',
        ssl = 'MONGODB_SSL' in environ
    )[environ['MONGODB_DATABASE']].people
except:
    _people = MongoClient()[environ['MONGODB_DATABASE']].people

def get_people():
    return _people.find(projection = {'_id': False})

def update_position(username, position):
    _people.update_one(
        {'username': username}, {'$set': {'position': position}}, True
    )
    return {'position': position, 'username': username}