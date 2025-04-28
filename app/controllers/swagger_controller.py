from flask import Blueprint, jsonify

swagger_blueprint = Blueprint('swagger', __name__)

@swagger_blueprint.route('/swagger.json')
def get_swagger():
    """Retorna a especificação do Swagger em formato JSON."""
    return jsonify({
        "swagger": "2.0",
        "info": {
            "title": "API de Gerenciamento de Produtos",
            "description": "API para gerenciamento de produtos com operações CRUD",
            "version": "1.0.0"
        },
        "basePath": "/api",
        "schemes": [
            "http",
            "https"
        ],
        "tags": [
            {
                "name": "produtos",
                "description": "Operações relacionadas a produtos"
            }
        ],
        "paths": {
            "/products": {
                "get": {
                    "tags": ["produtos"],
                    "summary": "Lista todos os produtos",
                    "description": "Retorna uma lista de todos os produtos cadastrados",
                    "produces": ["application/json"],
                    "responses": {
                        "200": {
                            "description": "Lista de produtos retornada com sucesso",
                            "schema": {
                                "type": "array",
                                "items": {"$ref": "#/definitions/Product"}
                            }
                        }
                    }
                },
                "post": {
                    "tags": ["produtos"],
                    "summary": "Cria um novo produto",
                    "description": "Adiciona um novo produto ao sistema",
                    "produces": ["application/json"],
                    "consumes": ["application/json"],
                    "parameters": [
                        {
                            "in": "body",
                            "name": "produto",
                            "description": "Objeto do produto a ser adicionado",
                            "required": True,
                            "schema": {"$ref": "#/definitions/ProductInput"}
                        }
                    ],
                    "responses": {
                        "201": {
                            "description": "Produto criado com sucesso",
                            "schema": {"$ref": "#/definitions/Product"}
                        },
                        "400": {
                            "description": "Dados inválidos"
                        }
                    }
                }
            },
            "/products/{product_id}": {
                "get": {
                    "tags": ["produtos"],
                    "summary": "Encontra produto por ID",
                    "description": "Retorna um único produto",
                    "produces": ["application/json"],
                    "parameters": [
                        {
                            "name": "product_id",
                            "in": "path",
                            "description": "ID do produto",
                            "required": True,
                            "type": "integer",
                            "format": "int64"
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Produto encontrado",
                            "schema": {"$ref": "#/definitions/Product"}
                        },
                        "404": {
                            "description": "Produto não encontrado"
                        }
                    }
                },
                "put": {
                    "tags": ["produtos"],
                    "summary": "Atualiza um produto existente",
                    "description": "Atualiza os dados de um produto pelo ID",
                    "produces": ["application/json"],
                    "consumes": ["application/json"],
                    "parameters": [
                        {
                            "name": "product_id",
                            "in": "path",
                            "description": "ID do produto a ser atualizado",
                            "required": True,
                            "type": "integer",
                            "format": "int64"
                        },
                        {
                            "in": "body",
                            "name": "produto",
                            "description": "Objeto produto com dados atualizados",
                            "required": True,
                            "schema": {"$ref": "#/definitions/ProductInput"}
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Produto atualizado com sucesso",
                            "schema": {"$ref": "#/definitions/Product"}
                        },
                        "400": {
                            "description": "Dados inválidos"
                        },
                        "404": {
                            "description": "Produto não encontrado"
                        }
                    }
                },
                "delete": {
                    "tags": ["produtos"],
                    "summary": "Remove um produto",
                    "description": "Exclui um produto pelo ID",
                    "produces": ["application/json"],
                    "parameters": [
                        {
                            "name": "product_id",
                            "in": "path",
                            "description": "ID do produto a ser removido",
                            "required": True,
                            "type": "integer",
                            "format": "int64"
                        }
                    ],
                    "responses": {
                        "204": {
                            "description": "Produto removido com sucesso"
                        },
                        "404": {
                            "description": "Produto não encontrado"
                        }
                    }
                }
            },
            "/products/name/{name}": {
                "get": {
                    "tags": ["produtos"],
                    "summary": "Busca produtos por nome",
                    "description": "Retorna produtos que contenham o nome especificado",
                    "produces": ["application/json"],
                    "parameters": [
                        {
                            "name": "name",
                            "in": "path",
                            "description": "Nome do produto (busca parcial)",
                            "required": True,
                            "type": "string"
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Lista de produtos encontrados",
                            "schema": {
                                "type": "array",
                                "items": {"$ref": "#/definitions/Product"}
                            }
                        }
                    }
                }
            },
            "/products/count": {
                "get": {
                    "tags": ["produtos"],
                    "summary": "Conta o número total de produtos",
                    "description": "Retorna a contagem de produtos cadastrados",
                    "produces": ["application/json"],
                    "responses": {
                        "200": {
                            "description": "Contagem retornada com sucesso",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "count": {
                                        "type": "integer",
                                        "description": "Número total de produtos"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "definitions": {
            "Product": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "format": "int64",
                        "description": "ID único do produto"
                    },
                    "name": {
                        "type": "string",
                        "description": "Nome do produto"
                    },
                    "description": {
                        "type": "string",
                        "description": "Descrição detalhada do produto"
                    },
                    "price": {
                        "type": "number",
                        "format": "float",
                        "description": "Preço do produto"
                    },
                    "stock_quantity": {
                        "type": "integer",
                        "format": "int32",
                        "description": "Quantidade em estoque"
                    },
                    "category": {
                        "type": "string",
                        "description": "Categoria do produto"
                    },
                    "created_at": {
                        "type": "string",
                        "format": "date-time",
                        "description": "Data de criação"
                    },
                    "updated_at": {
                        "type": "string",
                        "format": "date-time",
                        "description": "Data da última atualização"
                    }
                }
            },
            "ProductInput": {
                "type": "object",
                "required": ["name", "price"],
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Nome do produto"
                    },
                    "description": {
                        "type": "string",
                        "description": "Descrição detalhada do produto"
                    },
                    "price": {
                        "type": "number",
                        "format": "float",
                        "description": "Preço do produto"
                    },
                    "stock_quantity": {
                        "type": "integer",
                        "format": "int32",
                        "description": "Quantidade em estoque"
                    },
                    "category": {
                        "type": "string",
                        "description": "Categoria do produto"
                    }
                }
            }
        }
    })