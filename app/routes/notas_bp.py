from flask import Blueprint
from flask import jsonify, request
from ..extensions import db
from ..models.notas import Notas

notes = Blueprint('notas', __name__)

# Nuestro CRUD
@notes.route('/makenote', methods=['POST']) 
def makenotes():
    datos = request.get_json()
    
    #nueva_nota = Notas(titulo=datos["titulo"], nota=datos["nota"])
    try:
        nueva_nota = Notas(titulo=datos["titulo"], nota=datos["nota"])
        db.session.add(nueva_nota)
        db.session.commit()
        return jsonify({"mensaje": "Nota creada"}), 201
    except KeyError as key:
        db.session.rollback()
        return jsonify({"mensaje": f"Falta agregar los datos para la siguiente clave: {key}"}), 400
    finally:
        db.session.rollback()
        return jsonify({"mensaje": "Ocurrio un error inesperado"}), 400
     