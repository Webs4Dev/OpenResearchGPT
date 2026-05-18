from pydantic import BaseModel
from typing import Optional

class Paper(BaseModel):
    title: str
    abstract: Optional[str] = None
    authors: list[str]
    published_year: Optional[int] = None
    url: Optional[str] = None
    source: str