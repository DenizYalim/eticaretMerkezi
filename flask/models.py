from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    seller_id = db.Column(db.Integer)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    user = db.Column(db.String(100))
    text = db.Column(db.String(300))
    rating = db.Column(db.Integer)
    platform = db.Column(db.String(100))