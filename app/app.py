from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__)
CORS(app)
#configuro la basa de datos root:root@localhost/flaskmysql, se pone user:clave@localhost/nombreBaseDatos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:LUANa232@localhost/somaLibros'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
ma=Marshmallow(app)

#Vamos a definir la tabla
class Book (db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100))
    author=db.Column(db.String(100))
    editorial=db.Column(db.String(100))
    price=db.Column(db.Float)
    category=db.Column(db.String(100))
    description=db.Column(db.String(100))
    image=db.Column(db.String(100))
    state=db.Column(db.String(100))
    
    def __init__(self, title, author, editorial, price, category, description, image, state):
        self.title=title
        self.author=author
        self.editorial=editorial
        self.price=price
        self.category=category
        self.description=description
        self.image=image
        self.state=state
            
db.create_all() #crea la tabla

class bookSchema(ma.Schema):
    class Meta:
        fields=('id','title','author','editorial','price','category','description','image','state')
book_Schema=bookSchema() #creo el objeto para serializar
books_Schema=bookSchema(many=True) #creo el objeto para serializar varios registros

#Vamos a definir la ruta
@app.route('/books', methods=['GET']) #metodo GET
def get_books():
    all_books=Book.query.all() #obtengo todos los registros de la tabla
    result=books_Schema.dump(all_books) #serializo los registros
    return jsonify(result) #devuelvo el resultado

@app.route('/books/<id>', methods=['GET']) #metodo GET
def get_book(id):
    book=Book.query.get(id) #obtengo el registro con el id indicado
    return book_Schema.jsonify(book) #devuelvo el resultado

#Vamos a definir la ruta
@app.route('/books', methods=['POST']) #metodo POST
def post_book():
    title=request.json['title']
    author=request.json['author']
    editorial=request.json['editorial']
    price=request.json['price']
    category=request.json['category']
    description=request.json['description']
    image=request.json['image']
    state=request.json['state']
    
    new_book=Book(title, author, editorial, price, category, description, image, state)
    db.session.add(new_book)
    db.session.commit()
    return book_Schema.jsonify(new_book)

@app.route('/books/<id>', methods=['DELETE']) #metodo DELETE
def delete_book(id):
    book=Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return book_Schema.jsonify(book)

    


if __name__ == '__main__':
    app.run(debug=True, port=5000)