from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func
import models
import database
from pydantic_models import MovieBase, MoviePublic, SummaryRequest, SummaryResponse
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not set in .env file")

app = FastAPI()

# Initialize Groq LLM
llm = ChatGroq(model="mixtral-8x7b-32768", api_key=GROQ_API_KEY)

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/movies/", response_model=MoviePublic)
def create_movie(movie: MovieBase, db: Session = Depends(get_db)):
    db_movie = models.Movies(title=movie.title, year=movie.year, director=movie.director)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    
    for actor in movie.actors:
        db_actor = models.Actors(actor_name=actor.actor_name, movie_id=db_movie.id)
        db.add(db_actor)
    
    db.commit()
    db.refresh(db_movie)
    return db_movie

@app.get("/movies/random/", response_model=MoviePublic)
def get_random_movie(db: Session = Depends(get_db)):
    movie = (
        db.query(models.Movies)
        .options(joinedload(models.Movies.actors))
        .order_by(func.random())
        .first()
    )
    if not movie:
        raise HTTPException(status_code=404, detail="No movies found")
    return movie

@app.post("/generate_summary/", response_model=SummaryResponse)
def generate_summary(request: SummaryRequest, db: Session = Depends(get_db)):
    movie = (
        db.query(models.Movies)
        .options(joinedload(models.Movies.actors))
        .filter(models.Movies.id == request.movie_id)
        .first()
    )
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    
    actor_list = ", ".join(actor.actor_name for actor in movie.actors) or "various actors"
    prompt_template = PromptTemplate(
        input_variables=["title", "year", "director", "actor_list"],
        template=(
            "Generate a short, engaging summary (2-3 sentences) for the movie '{title}' ({year}), "
            "directed by {director} and starring {actor_list}. "
            "Focus on the main theme or plot without spoilers."
        )
    )
    
    chain = prompt_template | llm
    summary = chain.invoke({
        "title": movie.title,
        "year": movie.year,
        "director": movie.director,
        "actor_list": actor_list
    })
    
    return SummaryResponse(summary_text=summary.content)