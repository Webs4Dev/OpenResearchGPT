from backend.retrieval.arxiv_retriever import search_papers as arxiv_search
from backend.retrieval.semantic_retriever import search_papers as semantic_search 
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
    
    return papers