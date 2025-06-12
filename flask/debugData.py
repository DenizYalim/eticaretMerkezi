from app import app, db, Product, Comment

with app.app_context():
    # Create sample data
    p1 = Product(name="Gaming Mouse", seller_id=1)
    p2 = Product(name="Keyboard", seller_id=1)

    c1 = Comment(product_id=1, user="Alice", text="Great!", rating=5, platform="n11")
    c2 = Comment(product_id=1, user="Bob", text="Not bad", rating=3, platform="trendyol")
    c3 = Comment(product_id=2, user="Charlie", text="Perfect", rating=4, platform="hepsiburada")

    # Add and commit
    db.session.add_all([p1, p2, c1, c2, c3])
    db.session.commit()
    print("Seeded database!")
