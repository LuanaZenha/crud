🎬 Streaming API - CRUD com FastAPI + MongoDB + Docker

Esse é um exemplo prático de uma API de cadastro de filmes para um serviço de streaming.
Ele implementa operações de CRUD (Create, Read, Update e Delete) utilizando:

FastAPI, MongoDB e Docker + Docker Compose

🚀 Funcionalidades

✅ Cadastrar um filme

✅ Listar todos os filmes

✅ Buscar um filme pelo ID

✅ Atualizar informações de um filme

✅ Deletar um filme


📂 Estrutura de Pastas
streaming-api/
│── app/
│   ├── main.py             # Ponto de entrada da aplicação FastAPI
│   ├── database.py         # Conexão com MongoDB
│   ├── models.py           # Modelos (Pydantic) usados na API
│   ├── routers/
│   │   ├── health.py       # Rota de verificação de status
│   │   └── movies.py       # Rotas CRUD para filmes
│── docker-compose.yml      # Orquestração com Docker Compose
│── requirements.txt        # Dependências do Python
│── .env.example            # Exemplo de variáveis de ambiente
│── README.md               # Documentação do projeto


⚙️ Tecnologias Utilizadas

Python 3.11

FastAPI 0.115.2

MongoDB 6.x

Uvicorn 

Docker + Docker Compose


▶️ Como Rodar o Projeto
1. Pré-requisitos

Python 3.11

Docker Desktop

Git


Para clonar o repositório 

git clone https://github.com/seu-usuario/streaming-api.git
cd streaming-api


Pra subir o docker foi usado

ls
docker-compose
docker-compose up --build

Criando assim um container mongo-db rodando o MongoDB
container fastapi-streaming rodando a API em http://localhost:8000





