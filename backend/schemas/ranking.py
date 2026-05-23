from pydantic import BaseModel

class Scores(BaseModel):
    topic_match: int
    project_relevance: int
    research_similarity: int
    recency: int
    potential_value: int
    pdf_availability: int

class RankingResult(BaseModel):
    paper_name: str
    source: str
    pdf_status: str
    paper_url: str
    scores: Scores
    total_score: int
    why_it_matches: list[str]
    useful_ideas: list[str]
    pdf_usefulness: str