from app import ma
from app.models.product import Product
from marshmallow import fields

class ProductSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Product
    
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    description = fields.String()
    price = fields.Float(required=True)
    stock_quantity = fields.Integer()
    category = fields.String()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

# Inicializa os esquemas
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
