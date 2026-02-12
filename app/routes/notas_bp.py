from flask import Blueprint
from flask import jsonify, request
from ..extensions import db
from ..models.notas import Notas

notes = Blueprint('notas', __name__)

# Nuestro CRUD
@notes.route('/makenote', methods=['POST']) 
def makenote():
    datos = request.get_json()
    
    nueva_nota = Notas(titulo = datos["titulo"], nota = dato["nota"])
    try:
        db.session.add(nueva_nota)
        db.session.commit()
        return jsonify({"mensaje": "Nota creada"}), 201
    except ValueError:
        db.session.rollback()
        return jsonify({"mensaje": "ocurrio un erro"}), 400
     