import datetime
import bcrypt
from src.database import DB
from flask import jsonify

class Auth(object):

    def __init__(self, username,password):
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        self.created_at = datetime.datetime.utcnow()
 
    def insert(self):
        data = {
            "username": self.username,
            "password": self.password
        }
        DB.insert(collection='Auths', data=data)

    @staticmethod
    def signin(username,password):
        auth = DB.find_one('Auths',{"username": username})
        if auth != None and bcrypt.checkpw(password.encode('utf8'), auth['password']):
            return auth

        return None
     