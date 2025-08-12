from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    year = Column(Integer, nullable=True)
    genres = Column(String(255), nullable=True)
    rating = Column(Float, nullable=True)
