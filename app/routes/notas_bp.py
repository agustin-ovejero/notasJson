from flask import Blueprint
from flask import jsonify, request
from ..extensions import db
from ..models.notas import Notas

notes = Blueprint('notas', __name__)

# Nuestro CRUD
@notes.route('/makenote', methods=['POST']) 
def makenotes():
    datos = request.get_json()
    
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

@notes.route('/seenote', methods=['GET'])     
def seenotes():
    notas = Notas.query.all()
    if not notas:
        return jsonify({"mensaje": "No hay notas"}), 400
    notas_en_json = [{"id": i.id ,"titulo": i.titulo, "nota": i.nota} for i in notas]
    return jsonify(notas_en_json), 200
    
@notes.route('/seenoteid/<int:note_id>', methods=['GET'])
def seenotesid(note_id):
    note = Notas.query.get(note_id)
    if not note:
        return jsonify({"mensaje": "No existe el id de la nota"})
    return jsonify({"id": note.id, "titulo": note.titulo, "nota": note.nota}), 200
    
    
@notes.route('/delnote/<title>', methods=['DELETE'])
def delnotes(title):
    note = Notas.query.filter_by(titulo=title).first()
    if not note:
        return jsonify({"mensaje": f"no se encontro una nota con el titulo {title}"}), 400
    try:
        db.session.delete(note)
        db.session.commit()
        return jsonify({"mensaje": "se ellimino la nota correctamenten"}), 200
    except Exception:
        db.session.rollback()
        return jsonify({"mensaje": "algo salio mal"}), 400 # Esto hay que cambiar
        
@notes.route('/updatenote/<int:id>', methods=['PUT'])
def updatenotes(id):
    note = Notas.query.get(id)
    if not note:
        return jsonify({"mensaje": "no existe nota con ese id"}), 404
    try:
        nuevos_datos = request.get_json()
        note.titulo, note.nota = nuevos_datos["titulo"], nuevos_datos["nota"]
        db.session.add(note)
        db.session.commit()
        return jsonify({"mensaje": "Se actualizo la nota correctamente"}), 200
    except Exception:
        db.session.rollback()
        return jsonify({"mensaje": "Algo salio mal"}), 400
        