from .database import Base, engine, SessionLocal
from .models import Movie

def seed():
    # create tables if not exist
    Base.metadata.create_all(bind=engine)

    demo = [
        Movie(title="The Matrix", year=1999, genres="Action|Sci-Fi", rating=8.7),
        Movie(title="Spirited Away", year=2001, genres="Animation|Fantasy", rating=8.6),
        Movie(title="The Social Network", year=2010, genres="Drama", rating=7.8),
    ]

    with SessionLocal() as db:
        if db.query(Movie).count() == 0:
            db.add_all(demo)
            db.commit()
