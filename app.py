
from flask import Flask, request, jsonify, render_template, redirect

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import templates, static
import os
import templates, static

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.shoestore')
ma = Marshmallow(app)
db = SQLAlchemy(app)


class Shoe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False)
    description = db.Column(db.String(144), unique=False)
    size = db.Column(db.String(144), unique=False)
    price = db.Column(db.String(144), unique=False)
    img = db.Column(db.String(144), unique=False)

    def __init__(self, name, description, size, price, img):
        self.name = name
        self.description = description
        self.size = size
        self.price = price
        self.img = img


class ShoeSchema(ma.Schema):
    class Meta:
        fields = ('name', 'description', 'size', 'price', 'img')



shoe_schema = ShoeSchema()
shoes_schema = ShoeSchema(many=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')




@app.route('/shoe', methods=['POST'])
def add_shoe():
    description = request.json['description']
    name = request.json['name']
    size = request.json['size']
    price = request.json['price']
    img = request.json['img']

    new_shoe = Shoe(name, description, size, price, img)

    db.session.add(new_shoe)
    db.session.commit()

    
    shoe = Shoe.query.get(new_shoe.id)

    return shoe_schema.jsonify(shoe)


@app.route('/shoes', methods=['GET'])
def get_shoes():
    all_shoes = Shoe.query.all()
    result = shoes_schema.dump(all_shoes)
    return jsonify(result)



@app.route('/shoe/<id>', methods=['GET'])
def get_shoe(id):
    shoe = Shoe.query.get(id)
    return shoe_schema.jsonify(shoe)



@app.route('/shoe/<id>', methods=['PUT'])
def shoe_update(id):
    shoe = Shoe.query.get(id)
    name = request.json['name']
    description = request.json['description']
    size = request.json['size']
    price = request.json['price']
    img = request.json['img']

    shoe.name = name
    shoe.description = description
    shoe.size = size
    shoe.price = price

    shoe.img = img


    db.session.commit()
    return shoe_schema.jsonify(shoe)

@app.route('/shoe/<id>', methods=['DELETE'])
def shoe_delete(id):
    shoe = Shoe.query.get(id)
    db.session.delete(shoe)
    db.session.commit()

    return 'Shoe was succesfully removed'


if __name__ == '__main__':
    app.run(debug=True)
    
    
