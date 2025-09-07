from fastapi import FastAPI
from app.routers import health, movies

app = FastAPI(title="StreamingAPI", version="0.1.0")

app.include_router(health.router)
app.include_router(movies.router)

@app.get("/")
def read_root():
    return {"message": "Bem vindo ao Streaming API!"}
