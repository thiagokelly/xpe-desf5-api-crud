from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService
from app.utils.exceptions import ResourceNotFoundException, BadRequestException
from typing import Dict, Any, Tuple

# Cria o blueprint para as rotas de produto
product_blueprint = Blueprint('product', __name__)

# Instancia o serviço
product_service = ProductService()

@product_blueprint.route('/products', methods=['GET'])
def get_all_products() -> Tuple[Dict[str, Any], int]:
    """
    Endpoint para listar todos os produtos
    ---
    responses:
      200:
        description: Lista de todos os produtos
    """
    products = product_service.find_all()
    return jsonify(products), 200

@product_blueprint.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id: int) -> Tuple[Dict[str, Any], int]:
    """
    Endpoint para buscar um produto pelo ID
    ---
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
        description: ID do produto
    responses:
      200:
        description: Produto encontrado
      404:
        description: Produto não encontrado
    """
    try:
        product = product_service.find_by_id(product_id)
        return jsonify(product), 200
    except ResourceNotFoundException as e:
        return jsonify({'message': str(e)}), 404

@product_blueprint.route('/products/name/<string:name>', methods=['GET'])
def get_products_by_name(name: str) -> Tuple[Dict[str, Any], int]:
    """
    Endpoint para buscar produtos pelo nome
    ---
    parameters:
      - name: name
        in: path
        type: string
        required: true
        description: Nome parcial do produto
    responses:
      200:
        description: Lista de produtos que correspondem ao nome
    """
    products = product_service.find_by_name(name)
    return jsonify(products), 200

@product_blueprint.route('/products/count', methods=['GET'])
def count_products() -> Tuple[Dict[str, Any], int]:
    """
    Endpoint para contar o número total de produtos
    ---
    responses:
      200:
        description: Número total de produtos
    """
    count = product_service.count()
    return jsonify({'count': count}), 200

@product_blueprint.route('/products', methods=['POST'])
def create_product() -> Tuple[Dict[str, Any], int]:
    """
    Endpoint para criar um novo produto
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: Product
          required:
            - name
            - price
          properties:
            name:
              type: string
              description: Nome do produto
            description:
              type: string
              description: Descrição do produto
            price:
              type: number
              description: Preço do produto
            stock_quantity:
              type: integer
              description: Quantidade em estoque
            category:
              type: string
              description: Categoria do produto
    responses:
      201:
        description: Produto criado com sucesso
      400:
        description: Dados inválidos
    """
    try:
        product_data = request.get_json()
        new_product = product_service.create(product_data)
        return jsonify(new_product), 201
    except BadRequestException as e:
        return jsonify({'message': str(e)}), 400

@product_blueprint.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id: int) -> Tuple[Dict[str, Any], int]:
    """
    Endpoint para atualizar um produto existente
    ---
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
        description: ID do produto
      - name: body
        in: body
        required: true
        schema:
          id: ProductUpdate
          properties:
            name:
              type: string
              description: Nome do produto
            description:
              type: string
              description: Descrição do produto
            price:
              type: number
              description: Preço do produto
            stock_quantity:
              type: integer
              description: Quantidade em estoque
            category:
              type: string
              description: Categoria do produto
    responses:
      200:
        description: Produto atualizado com sucesso
      404:
        description: Produto não encontrado
      400:
        description: Dados inválidos
    """
    try:
        product_data = request.get_json()
        updated_product = product_service.update(product_id, product_data)
        return jsonify(updated_product), 200
    except ResourceNotFoundException as e:
        return jsonify({'message': str(e)}), 404
    except BadRequestException as e:
        return jsonify({'message': str(e)}), 400

@product_blueprint.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id: int) -> Tuple[Dict[str, Any], int]:
    """
    Endpoint para excluir um produto
    ---
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
        description: ID do produto
    responses:
      204:
        description: Produto excluído com sucesso
      404:
        description: Produto não encontrado
    """
    try:
        product_service.delete(product_id)
        return '', 204
    except ResourceNotFoundException as e:
        return jsonify({'message': str(e)}), 404

# Middleware para tratamento global de exceções
@product_blueprint.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, ResourceNotFoundException):
        return jsonify({'message': str(e)}), 404
    elif isinstance(e, BadRequestException):
        return jsonify({'message': str(e)}), 400
    else:
        return jsonify({'message': 'Erro interno do servidor'}), 500
