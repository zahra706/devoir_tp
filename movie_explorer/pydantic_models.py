from pydantic import BaseModel
from typing import List

class ActorBase(BaseModel):
    actor_name: str

class MovieBase(BaseModel):
    title: str
    year: int
    director: str
    actors: List[ActorBase]

class ActorPublic(BaseModel):
    id: int
    actor_name: str
    class Config:
        from_attributes = True

class MoviePublic(BaseModel):
    id: int
    title: str
    year: int
    director: str
    actors: List[ActorPublic]
    class Config:
        from_attributes = True

class SummaryRequest(BaseModel):
    movie_id: int

class SummaryResponse(BaseModel):
    summary_text: str