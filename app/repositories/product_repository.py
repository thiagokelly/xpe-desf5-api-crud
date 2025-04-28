from app import db
from app.models.product import Product
from app.utils.exceptions import ResourceNotFoundException
from typing import List, Optional

class ProductRepository:
    def find_all(self) -> List[Product]:
        """Retorna todos os produtos."""
        return Product.query.all()
    
    def find_by_id(self, product_id: int) -> Product:
        """Busca um produto pelo ID."""
        product = Product.query.get(product_id)
        if not product:
            raise ResourceNotFoundException(f"Produto não encontrado com id: {product_id}")
        return product
    
    def find_by_name(self, name: str) -> List[Product]:
        """Busca produtos pelo nome (parcial)."""
        return Product.query.filter(Product.name.ilike(f'%{name}%')).all()
    
    def save(self, product: Product) -> Product:
        """Salva um produto."""
        db.session.add(product)
        db.session.commit()
        return product
    
    def update(self, product: Product) -> Product:
        """Atualiza um produto existente."""
        db.session.commit()
        return product
    
    def delete(self, product_id: int) -> None:
        """Remove um produto pelo ID."""
        product = self.find_by_id(product_id)
        db.session.delete(product)
        db.session.commit()
    
    def count(self) -> int:
        """Retorna o número total de produtos."""
        return Product.query.count()
