from fastapi import APIRouter, HTTPException
from app.database import db
from app.models import Movie
from bson import ObjectId

router = APIRouter(prefix="/movies", tags=["movies"])
collection = db["movies"]

def movie_serializer(movie) -> dict:
    return {
        "id": str(movie["_id"]),
        "title": movie["title"],
        "genre": movie["genre"],
        "year": movie["year"],
    }

@router.post("", response_model=dict)
def create_movie(movie: Movie):
    result = collection.insert_one(movie.dict())
    return {"id": str(result.inserted_id)}

@router.get("", response_model=list)
def list_movies():
    movies = list(collection.find())
    return [movie_serializer(m) for m in movies]

@router.get("/{movie_id}", response_model=dict)
def get_movie(movie_id: str):
    movie = collection.find_one({"_id": ObjectId(movie_id)})
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie_serializer(movie)

@router.put("/{movie_id}", response_model=dict)
def update_movie(movie_id: str, movie: Movie):
    result = collection.update_one(
        {"_id": ObjectId(movie_id)}, {"$set": movie.dict()}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"message": "Movie updated successfully"}

@router.delete("/{movie_id}", response_model=dict)
def delete_movie(movie_id: str):
    result = collection.delete_one({"_id": ObjectId(movie_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"message": "Movie deleted successfully"}
