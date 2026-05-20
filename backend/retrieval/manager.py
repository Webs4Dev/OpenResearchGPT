from backend.retrieval.retriever_arxiv import search_papers as arxiv_search
from backend.retrieval.retriever_semantic import search_papers as semantic_search 
from backend.retrieval.retriever_pubmed import search_papers as pubmed_search
from backend.retrieval.retriever_openalex import search_papers as openalex_search
from backend.retrieval.retriever_crossref import search_papers as crossref_search
from backend.utils.logger import log

papers = []
def retrieve_all(query:str,max_results:int):
    try:
        log("Searching arXiv...")
        papers.extend(
            arxiv_search(
                query=query,
                max_results=max_results
                )
        )
    except Exception as e:
        print(f"Error while getting arxiv paper : {e}")

    try:
        log("Searching Semantic Scholar...")
        papers.extend(
            semantic_search(
                query=query,
                max_results=max_results
                )
        )
    except Exception as e:
        print(f"Error while getting semantic scholar paper : {e}")

    try:
        log("Searching PubMed...")
        papers.extend(
            pubmed_search(
                query=query,
                max_results=max_results
                )
        )
    except Exception as e:
        print(f"Error while getting pubmed paper : {e}")

    try:
        log("Searching OpenAlex...")
        papers.extend(
            openalex_search(
                query=query,
                max_results=max_results
                )
        )
    except Exception as e:
        print(f"Error while getting openalex paper : {e}")

    try:
        log("Searching CrossRef...")
        papers.extend(
            crossref_search(
                query=query,
                max_results=max_results
                )
        )
    except Exception as e:
        print(f"Error while getting crossref paper : {e}")
    
    return papers