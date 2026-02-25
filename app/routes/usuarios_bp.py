# Archivo para ver si funciona la creacion de usuarios 

import json
from flask import Blueprint
from flask import request, jsonify
from ..extensions import db
from ..models.user import Usuario
from werkzeug.security import generate_password_hash

users = Blueprint('users', __name__)

@users.route('/makeuser', methods=['POST'])
def make_user():
    datos = request.get_json()
    try:
        nuevo_usuario = Usuario(
            nombre = datos["nombre"],
            email = datos["email"],
            password_hash = generate_password_hash(datos["password_hash"])
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        return jsonify({"mensaje": "usuario creado correctamente"}), 200
    except Exception:
        return jsonify({"mensaje": "algo salio mal"}), 400


@users.route('/seeusers', methods=['GET'])
def see_users():
    usuarios = Usuario.query.all()
    
    if not usuarios:
        return jsonify({'mensaje': 'no hay ningun usuario  creado'}), 400
    
    usuarios_dict = [{"id": i.id, "nombre": i.nombre, "email": i.email, "contrasena": i.password_hash} for i in usuarios]
    return jsonify(usuarios_dict)
    