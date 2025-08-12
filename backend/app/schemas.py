from pydantic import BaseModel

class MovieRead(BaseModel):
    id: int
    title: str
    year: int | None = None
    genres: str | None = None
    rating: float | None = None

    class Config:
        from_attributes = True  # pydantic v2
