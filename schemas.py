from pydantic import BaseModel
from datetime import date


class AuthorBaseSchema(BaseModel):
    name: str
    bio: str


class AuthorCreateSchema(AuthorBaseSchema):
    pass


class AuthorSchema(AuthorBaseSchema):
    id: int

    class Config:
        orm_mode = True


class BookBaseSchema(BaseModel):
    title: str
    summary: str
    publication_date: date


class BookCreateSchema(BookBaseSchema):
    pass


class BookSchema(BookBaseSchema):
    id: int

    class Config:
        orm_mode = True
