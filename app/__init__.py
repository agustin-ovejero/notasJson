from flask import Flask
from .extensions import db
from config import sqlalchemy_database_uri
def create_app():
   app = Flask(__name__) 
   app.config.from_object(sqlalchemy_database_uri)
   db.init_app(app)
   with app.app_context():
       db.create_all()
   return app