from pydantic import BaseModel

class Filme(BaseModel):
    titulo: str
    genero: str
    ano: int