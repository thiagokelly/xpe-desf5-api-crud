
# 📦 Sistema de Gerenciamento de Produtos

Este projeto é uma API RESTful desenvolvida com **Flask**, **SQLAlchemy** e **Marshmallow** para gerenciar produtos, permitindo operações de **CRUD**, **busca por nome**, **contagem de produtos** e **documentação via Swagger UI**.

---

## 🚀 Tecnologias Utilizadas

- Python 3.10+
- Flask 2.2.3
- Flask-SQLAlchemy 3.0.3
- Flask-Marshmallow 0.14.0
- Marshmallow-SQLAlchemy 0.29.0
- Python-dotenv 1.0.0
- Flask-Swagger-UI 4.11.1
- Pytest 7.3.1
- SQLite (default para dev/teste) e suporte a PostgreSQL (produção)

---

## 🛠️ Estrutura do Projeto

```
app/
├── __init__.py         # Inicialização da aplicação e extensões
├── config.py           # Configurações (dev/test/prod)
├── swagger.py           # Configurações do Swagger(dev/test/prod)
├── models/
│   └── product.py      # Modelo do Produto
├── dto/
│   └── product_dto.py  # Schema de serialização/desserialização
├── repositories/
│   └── product_repository.py # Acesso ao banco de dados
├── services/
│   └── product_service.py    # Regras de negócio
├── controllers/
│   └── product_controller.py # Rotas da API
├── utils/
│   └── exceptions.py   # Tratamento de exceções personalizadas
diagrams/               # Diagramas da aplicação
main.py                  # Arquivo principal para execução
requirements.txt        # Dependências do projeto
README.md               # Explicação de funcionamento da app
```

---

## ⚙️ Configuração e Execução

### 1. Clonar o repositório

```bash
git clone https://github.com/thiagokelly/xpe-desf5-api-crud.git
cd xpe-desf5-api-crud
```

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente (opcional)

Crie um arquivo `.env` na raiz do projeto, se desejar sobrescrever configurações:

```
APP_SETTINGS=app.config.DevelopmentConfig
SECRET_KEY=sua_chave_secreta
DATABASE_URL=postgresql://usuario:senha@localhost/seu_banco
```

### 5. Executar a aplicação

```bash
python main.py
```

Por padrão, a aplicação ficará disponível em:

```
http://localhost:5000
```

---

## 🧪 Testes

Os testes podem ser implementados usando **pytest**. Para rodá-los:

```bash
pytest
```

(⚠️ Observação: o projeto ainda não contém arquivos de teste prontos.)

---

## 📚 Documentação da API

A documentação interativa da API estará disponível após iniciar a aplicação:

```
http://localhost:5000/api/docs
```

---

## 📖 Principais Endpoints

| Método | Rota                         | Descrição                           |
|--------|-------------------------------|-------------------------------------|
| GET    | `/api/products`               | Listar todos os produtos            |
| GET    | `/api/products/<id>`           | Buscar produto por ID               |
| GET    | `/api/products/name/<name>`    | Buscar produtos por nome (parcial)  |
| GET    | `/api/products/count`          | Contar total de produtos            |
| POST   | `/api/products`                | Criar um novo produto               |
| PUT    | `/api/products/<id>`            | Atualizar um produto existente      |
| DELETE | `/api/products/<id>`            | Excluir um produto                  |

---

## 🧩 Sobre a Arquitetura

- **Camadas separadas**: controllers, services, repositories, models e DTOs para melhor organização e manutenção.
- **Tratamento centralizado de exceções** usando classes customizadas.
- **Suporte a múltiplos ambientes** (desenvolvimento, teste e produção).
- **Facilidade de extensão** para novos recursos.

---

## 📌 Melhorias Futuras

- Implementar testes unitários e de integração.
- Melhorar autenticação/autorização.
- Versionamento da API.
- Deploy automático (Docker, CI/CD).
- Integração completa do Swagger UI.

---

## 🧑‍💻 Autor

Feito por Thiago Kelly.

---

