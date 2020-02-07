from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import templates, static

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.shoestore')
ma = Marshmallow(app)
db = SQLAlchemy(app)


# This is building and assigning the key value pairs, or database layout or format, within the database
class Shoe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False)
    description = db.Column(db.String(144), unique=False)
    size = db.Column(db.String(144), unique=False)
    price = db.Column(db.String(144), unique=False)

    def __init__(self, name, description, size, price):
        self.name = name
        self.description = description
        self.size = size
        self.price = price


class ShoeSchema(ma.Schema):
    class Meta:
        fields = ('name', 'description', 'size', 'price', 'id')


shoe_schema = ShoeSchema()
shoes_schema = ShoeSchema(many=True)

@app.route('/')
def home():
    return render_template('index.html')


# Endpoint to create a new guide

@app.route('/shoe', methods=['POST'])
def add_shoe():
    name = request.json['name']
    description = request.json['description']
    size = request.json['size']
    price = request.json['price']

    new_shoe = Shoe(name, description, size, price)

    db.session.add(new_shoe)
    db.session.commit()

    
    shoe = Shoe.query.get(new_shoe.id)

    return shoe_schema.jsonify(shoe)


# endpoint to query all guides
@app.route('/shoes', methods=['GET'])
def get_shoes():
    all_shoes = Shoe.query.all()
    result = shoes_schema.dump(all_shoes)
    return jsonify(result)


# endpoint for querying a single guide
@app.route('/shoe/<id>', methods=['GET'])
def get_shoe(id):
    shoe = Shoe.query.get(id)
    return shoe_schema.jsonify(shoe)


# endpoint for updating a guide
@app.route('/shoe/<id>', methods=['PUT'])
def shoe_update(id):
    shoe = Shoe.query.get(id)
    name = request.json['name']
    description = request.json['description']
    size = request.json['size']
    price = request.json['price']

    shoe.name = name
    shoe.description = description
    shoe.size = size
    shoe.price = price

    db.session.commit()
    return shoe_schema.jsonify(shoe)

# endpoint for deleting a record
@app.route('/shoe/<id>', methods=['DELETE'])
def shoe_delete(id):
    shoe = Shoe.query.get(id)
    db.session.delete(shoe)
    db.session.commit()

    return 'Shoe was succesfully removed'


if __name__ == '__main__':
    app.run(debug=True)
