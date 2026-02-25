from flask import Flask
from .extensions import db
from flask_migrate import Migrate
from config import Config

from .routes.index import index
from .routes.notas_bp import notes
from .routes.usuarios_bp import users


def create_app():
   app = Flask(__name__) 
   app.config.from_object(Config) # El metodo from_object solamente acepta clases que las va a escanear
   db.init_app(app)
   from .models import notas, user
   migrate = Migrate(app, db)
   
   # |-- rutas --|
   app.register_blueprint(index)
   app.register_blueprint(notes)
   app.register_blueprint(users)
   
   
  
   # with app.app_context():
   #     db.create_all()
   return app