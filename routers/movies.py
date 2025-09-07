from fastapi import APIRouter, HTTPException
from app.database import db
from app.models import movies
from bson import ObjectId

router = APIRouter(prefix="/movies", tags=["movies"])
collection = db["movies"]

def movies_serializer(movie) -> dict:
    return {
        "id": str(movie["_id"]),
        "titulo": movie["titulo"],
        "genero": movie["genero"],
        "ano": movie["ano"]
    }
