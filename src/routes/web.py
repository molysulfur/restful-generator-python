from flask import Blueprint , render_template,request ,jsonify
from src.models.auth import Auth
import datetime
from bson import json_util
import json
import bcrypt
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
    )
    
route = Blueprint('web', __name__)

def get_blueprint():
    """Return the blueprint for the main app module"""
    return route

@route.route('/')
def index():
    """Main page route."""
    button_text = "Add Job"
    return render_template('main.html', button_text=button_text)

@route.route('/signup')
def signup():
    return render_template('signup.html')

@route.route('/add_user',methods=["POST"])
def addUser():
    username = request.form['username']
    password = request.form['password']
    auth = Auth(username=username,password=password)
    auth.insert()
    return ('', 200)

@route.route('/signin',methods=["POST"])
def signin():
    username = request.form['username']
    password = request.form['password']
    expired = datetime.timedelta(days=1)
    response = Auth.signin(username=username,password=password)
    if response != None :
        access_token = create_access_token(identity=username,expires_delta=expired)
        refresh_token = create_refresh_token(identity=username)
        return ({'expired': int(datetime.datetime.timestamp(datetime.datetime.utcnow() + expired)),'access_token' : access_token,'refresh_token': refresh_token}, 200)

    return ({'code':401,'message': "username and/or password is not vaild"},401)