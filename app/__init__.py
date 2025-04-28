# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Inicializa extensões
db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    # Inicializa a aplicação Flask
    app = Flask(__name__)
    
    # Carrega as configurações
    app_settings = os.getenv('APP_SETTINGS', 'app.config.DevelopmentConfig')
    app.config.from_object(app_settings)
    
    # Inicializa os plugins
    db.init_app(app)
    ma.init_app(app)
    
    # Importa e registra os blueprints
    from app.controllers.product_controller import product_blueprint
    app.register_blueprint(product_blueprint, url_prefix='/api')
    
    # Registra o blueprint do Swagger
    # Importamos as variáveis do módulo swagger também
    from app.swagger import swagger_ui_blueprint, SWAGGER_URL
    app.register_blueprint(swagger_ui_blueprint)
    
    # Registra o blueprint que fornece o arquivo swagger.json
    from app.controllers.swagger_controller import swagger_blueprint
    app.register_blueprint(swagger_blueprint, url_prefix='/api')
    
    # Cria as tabelas do banco de dados
    with app.app_context():
        db.create_all()
    
    return app