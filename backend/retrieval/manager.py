from backend.retrieval.retriever_arxiv import search_papers as arxiv_search
from backend.retrieval.retriever_semantic import search_papers as semantic_search
from backend.retrieval.retriever_pubmed import search_papers as pubmed_search
from backend.retrieval.retriever_openalex import search_papers as openalex_search
from backend.retrieval.retriever_crossref import search_papers as crossref_search
from backend.utils.logger import log

ALL_SOURCES = {
    "arxiv": arxiv_search,
    "semantic_scholar": semantic_search,
    "pubmed": pubmed_search,
    "openalex": openalex_search,
    "crossref": crossref_search,
}

def retrieve_all(query: str,max_results: int,sources: list[str] | None = None) -> tuple[list, dict]:
    """
    Returns:
        papers        - flat list of Paper objects
        source_report - { source_name: { count, status, error } }
    """

    active = sources if sources else list(ALL_SOURCES.keys())
    unknown = [s for s in active if s not in ALL_SOURCES]

    if unknown:
        raise ValueError(f"Unknown sources: {unknown}. Valid: {list(ALL_SOURCES.keys())}")

    papers = []     
    report = {}

    for name in active:
        log(f"Searching {name}...")
        try:
            results = ALL_SOURCES[name](query=query, max_results=max_results)
            papers.extend(results)
            report[name] = {"count": len(results), "status": "ok", "error": None}
            log(f"[{name}] → {len(results)} papers")
        except Exception as e:
            report[name] = {"count": 0, "status": "error", "error": str(e)}
            log(f"[{name}] failed: {e}")

    return papers, report