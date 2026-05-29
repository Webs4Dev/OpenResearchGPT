from pydantic import BaseModel
from typing import Optional

class Paper(BaseModel):
    title: str
    abstract: Optional[str] = None
    authors: list[str]
    published_year: Optional[int] = None
    url: Optional[str] = None
    citation_count: int = 0
    source: str