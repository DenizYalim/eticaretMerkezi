from flask import Flask, jsonify
from flask_cors import CORS
from models import db, Product, Comment

app = Flask(__name__)
CORS(app)

# DB config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# API Routes
@app.route('/api/products/<int:seller_id>')
def get_products(seller_id):
    products = Product.query.filter_by(seller_id=seller_id).all()
    return jsonify([{"id": p.id, "name": p.name} for p in products])

@app.route('/api/comments/<int:product_id>')
def get_comments(product_id):
    comments = Comment.query.filter_by(product_id=product_id).all()
    return jsonify([{
        "platform": c.platform,
        "user": c.user,
        "text": c.text,
        "rating": c.rating
    } for c in comments])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # creates data.db on first run
    app.run(debug=True)
