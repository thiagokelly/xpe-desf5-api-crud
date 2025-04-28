from flask_swagger_ui import get_swaggerui_blueprint

# Configuração do Swagger UI
SWAGGER_URL = '/api/docs'  # URL para acessar a UI do Swagger
API_URL = '/api/swagger.json'  # URL para o arquivo de especificação do Swagger

# Cria o blueprint do Swagger UI
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API de Gerenciamento de Produtos"
    }
)