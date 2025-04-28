from app import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, default=0)
    category = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    def __init__(self, name, description=None, price=0, stock_quantity=0, category=None):
        self.name = name
        self.description = description
        self.price = price
        self.stock_quantity = stock_quantity
        self.category = category
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def update_timestamp(self):
        self.updated_at = datetime.now()
