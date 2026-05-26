from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

from backend.retrieval.manager import retrieve_all, ALL_SOURCES
from backend.agents.ranking_agent import rank_paper
from backend.utils.logger import log

router = APIRouter()

class SearchRequest(BaseModel):
    query: str
    project_description: Optional[str] = None   
    max_results_per_source: Optional[int] = 5
    sources: Optional[list[str]] = None           

class SourceReport(BaseModel):
    count: int
    status: str
    error: Optional[str]


class SearchResponse(BaseModel):
    query: str
    sources_requested: list[str]
    total_papers_retrieved: int
    total_ranked: int
    source_report: dict[str, SourceReport]
    ranked_results: list

@router.get("/sources")
def list_sources():
    """Return all available retrieval sources."""
    return {
        "available_sources": list(ALL_SOURCES.keys()),
        "total": len(ALL_SOURCES)
    }


@router.post("/search", response_model=SearchResponse)
async def search_and_rank(request: SearchRequest):

    if not request.query.strip():
        raise HTTPException(status_code=400,detail="Query cannot be empty")

    if request.sources:
        invalid = [source for source in request.sources if source not in ALL_SOURCES]
        if invalid:
            raise HTTPException(status_code=400,detail=f"Invalid sources: {invalid}")

    active_sources = (request.sources or list(ALL_SOURCES.keys()))

    try:
        papers, report = retrieve_all(
            query=request.query,
            max_results=request.max_results_per_source,
            sources=active_sources
        )

    except Exception as e:
        log(f"Retrieval Error: {e}")
        raise HTTPException(
            status_code=500,
            detail="Retrieval failed"
        )

    if not papers:
        return SearchResponse(
            query=request.query,
            sources_requested=active_sources,
            total_papers_retrieved=0,
            total_ranked=0,
            source_report={k: SourceReport(**v) for k, v in report.items()},
            ranked_results=[]
        )

    ranked = []
    for paper in papers:
        try:
            result = rank_paper(
                query=request.query,
                paper=paper,
                project_description=request.project_description
            )
            ranked.append(result)
        except Exception as e:
            log(f"Ranking skipped for '{paper.title}': {e}")
            continue   

    ranked.sort(key=lambda r: r.total_score, reverse=True)

    return SearchResponse(
        query=request.query,
        sources_requested=active_sources,
        total_papers_retrieved=len(papers),
        total_ranked=len(ranked),
        source_report={k: SourceReport(**v) for k, v in report.items()},
        ranked_results=[r.model_dump() for r in ranked]
    )