from pydantic import BaseModel

class User(BaseModel):
    id:int
    movie_name:str
    director_name:str
    synopsis:str