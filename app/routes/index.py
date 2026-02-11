from flask import Blueprint

index = Blueprint('index', __name__)
@index.route('/')
def indice():
    return "<h1>Hello World<h1>"
    