from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

from .database import SessionLocal
from . import models, schemas
from .seed import seed

app = FastAPI(title="Movie Recommender API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def on_startup():
    seed()

@app.get("/", tags=["health"])
def root():
    return {"message": "Backend running"}

@app.get("/movies", response_model=List[schemas.MovieRead], tags=["movies"])
def list_movies(db: Session = Depends(get_db)):
    return db.query(models.Movie).order_by(models.Movie.id.asc()).all()
