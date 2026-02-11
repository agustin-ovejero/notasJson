from flask import Flask
from .extensions import db
from config import Config

from .routes.index import index
def create_app():
   app = Flask(__name__) 
   app.register_blueprint(index)
   
   
   app.config.from_object(Config) # El metodo from_object solamente acepta clases que las va a escanear
   db.init_app(app)
   with app.app_context():
       db.create_all()
   return app