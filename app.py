import os
import json
import datetime
from bson.objectid import ObjectId
from flask import Flask , render_template
from src.models.auth import Auth
from src.database import DB
from src.routes import web
from flask_jwt_extended import JWTManager

"""
    Change path templates
"""
project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'src/templates')

app = Flask(__name__,template_folder=template_path)
app.config['JWT_SECRET_KEY'] = 'JWT_SECRET_KEY'
jwt = JWTManager(app)
DB.init()
app.register_blueprint(web.get_blueprint())

if __name__ == "__main__":
    app.run(debug=True)