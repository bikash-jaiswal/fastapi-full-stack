from pydantic import BaseModel


class BlogModel(BaseModel):
    id: str
    title: str
    author: str
    content: str
    publication_date: str
