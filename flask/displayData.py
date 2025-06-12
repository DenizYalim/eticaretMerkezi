from app import app, db
from models import Product, Comment  # adjust import paths to your setup

with app.app_context():
    comments = Comment.query.all()
    for c in comments:
        print(f"Platform: {c.platform},Product ID: {c.product_id}, User: {c.user}, Text: {c.text}, Rating: {c.rating}")
