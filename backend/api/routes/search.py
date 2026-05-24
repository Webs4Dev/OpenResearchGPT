from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

from backend.retrieval.manager import retrieve_all
from backend.agents.ranking_agent import rank_paper

router = APIRouter()

class SearchRequest(BaseModel):
    query: str
    project_description: Optional[str]
    max_results_per_source: Optional[int] = 5

class SearchResponse(BaseModel):
    query: str
    total_papers_retrieved: int
    ranked_results: list

@router.post("/search", response_model=SearchResponse)
async def search_and_rank(request: SearchRequest):
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty.")

    papers = retrieve_all(
        query=request.query,
        max_results=request.max_results_per_source
    )

    if not papers:
        return SearchResponse(
            query=request.query,
            total_papers_retrieved=0,
            ranked_results=[]
        )

    ranked = rank_paper(
        paper=papers,
        query=request.query,
        project_description=request.project_description
    )

    return SearchResponse(
        query=request.query,
        total_papers_retrieved=len(papers),
        ranked_results=[r.model_dump() for r in ranked]
    )

