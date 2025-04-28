from app.repositories.product_repository import ProductRepository
from app.models.product import Product
from app.dto.product_dto import product_schema, products_schema
from app.utils.exceptions import ResourceNotFoundException, BadRequestException
from typing import List, Dict, Any

class ProductService:
    def __init__(self):
        self.repository = ProductRepository()
    
    def find_all(self) -> List[Dict[str, Any]]:
        """Retorna todos os produtos."""
        products = self.repository.find_all()
        return products_schema.dump(products)
    
    def find_by_id(self, product_id: int) -> Dict[str, Any]:
        """Busca um produto pelo ID."""
        product = self.repository.find_by_id(product_id)
        return product_schema.dump(product)
    
    def find_by_name(self, name: str) -> List[Dict[str, Any]]:
        """Busca produtos pelo nome (parcial)."""
        products = self.repository.find_by_name(name)
        return products_schema.dump(products)
    
    def create(self, product_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria um novo produto."""
        try:
            # Valida e deserializa os dados
            validated_data = product_schema.load(product_data)
            
            # Cria um novo produto
            product = Product(
                name=validated_data.get('name'),
                description=validated_data.get('description'),
                price=validated_data.get('price'),
                stock_quantity=validated_data.get('stock_quantity', 0),
                category=validated_data.get('category')
            )
            
            # Salva o produto
            saved_product = self.repository.save(product)
            return product_schema.dump(saved_product)
        except Exception as e:
            raise BadRequestException(str(e))
    
    def update(self, product_id: int, product_data: Dict[str, Any]) -> Dict[str, Any]:
        """Atualiza um produto existente."""
        try:
            # Busca o produto existente
            existing_product = self.repository.find_by_id(product_id)
            
            # Atualiza os campos
            if 'name' in product_data:
                existing_product.name = product_data['name']
            if 'description' in product_data:
                existing_product.description = product_data['description']
            if 'price' in product_data:
                existing_product.price = product_data['price']
            if 'stock_quantity' in product_data:
                existing_product.stock_quantity = product_data['stock_quantity']
            if 'category' in product_data:
                existing_product.category = product_data['category']
            
            # Atualiza o timestamp
            existing_product.update_timestamp()
            
            # Salva as alterações
            updated_product = self.repository.update(existing_product)
            return product_schema.dump(updated_product)
        except ResourceNotFoundException as e:
            raise e
        except Exception as e:
            raise BadRequestException(str(e))
    
    def delete(self, product_id: int) -> None:
        """Remove um produto pelo ID."""
        self.repository.delete(product_id)
    
    def count(self) -> int:
        """Retorna o número total de produtos."""
        return self.repository.count()