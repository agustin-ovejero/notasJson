from sqlite3.dbapi2 import DatabaseError

from flask import Flask, jsonify, request

from database import db
from models import Notas

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notasjson.db"
db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return "<h1>hello world<h1"


@app.route("/seenote", methods=["GET"])
def ver_nota():
    notas = Notas.query.all()  # esta manera obtenemos todos las notas de la db
    en_json = [{"id": i.id, "titulo": i.titulo, "nota": i.nota} for i in notas]

    return jsonify(en_json)


@app.route("/idnote/<int:id>", methods=["GET"])
def nota_id(id):

    try:
        nota = Notas.query.get(id)
        return jsonify({"id": nota.id, "titulo": nota.titulo, "nota": nota.nota}), 200
    except ValueError:
        return jsonify({"mensje": "algo salio mal"})


@app.route("/delnote/<titulo>", methods=["DELETE"])
def eliminando_nota(titulo):
    if titulo is None:
        return jsonify({"mensja": "no ingresaste el titulo"})
    nota = Notas.query.filter_by(titulo=titulo).first()
    if not nota:
        return jsonify({"mensaje": "la nota no existe"}), 404
    try:
        db.session.delete(nota)
        db.session.commit()
        return jsonify({"mensaje": "nota eliminada"}), 200
    except Exception:
        db.session.rollback()
        return jsonify({"mensaje": "error db"})


@app.route("/makenote", methods=["POST"])
def crear_nota():
    datos = (
        request.get_json()
    )  # de esta manera obtenemos los datos pasados en formato json

    nueva_nota = Notas(  # de esta manera creamos el dato que envuelve todos los datos de para la base
        titulo=datos["titulo"],
        nota=datos["nota"]
    )

    try:
        db.session.add(nueva_nota)  # agregamos a la base
        db.session.commit()  # guardamos en la base
        return jsonify({"mensaje": "nota creada"}), 201
    except ValueError:
        db.session.rollback()
        return jsonify({"mensaje": "existe ese titulo"}), 400


if __name__ == "__main__":
    app.run(debug=True)
