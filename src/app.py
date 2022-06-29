from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:LUANa232@localhost/somalibros'
#                                               user:clave@localhost/nombreBaseDatos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db= SQLAlchemy(app)
ma=Marshmallow(app)

class libro (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    autor = db.Column(db.String(100))
    editorial = db.Column(db.String(100))
    precio = db.Column(db.String(100))
    categoria = db.Column(db.String(100))
    descripcion = db.Column(db.String(100))
    portada = db.Column(db.String(100))
    estado = db.Column(db.String(100))
    def __init__(self, titulo, autor, editorial, precio, categoria, descripcion, portada, estado):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.precio = precio
        self.categoria = categoria
        self.descripcion = descripcion
        self.portada = portada
        self.estado = estado

db.create_all()

class LibroSchema(ma.Schema):
    class Meta:
        fields = ('id', 'titulo', 'autor', 'editorial', 'precio', 'categoria', 'descripcion', 'portada', 'estado')
libro_schema = LibroSchema()
libros_schema = LibroSchema(many=True)

@app.route('/libros', methods=['GET'])
def get_libros():
    all_libros = libro.query.all()
    result = libros_schema.dump(all_libros)
    return jsonify(result)

@app.route('/libro/<id>', methods=['GET'])
def get_libro(id):
    libro = libro.query.get(id)
    result = libro_schema.dump(libro)
    return libro_schema.jsonify(result)


# programa principal
if __name__=='__main__':  
    app.run(debug=True, port=5000)  
