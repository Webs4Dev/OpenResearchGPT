from backend.retrieval.arxiv_retriever import search_papers as arxiv_search
from backend.retrieval.semantic_retriever import search_papers as semantic_search

papers=[]

papers.extend(
    arxiv_search(
        query="multi agent memory systems",
        max_results=1
    )
)

papers.extend(
    semantic_search(
        query="multi agent memory systems",
        max_results=1
    )
)

for paper in papers:

    print("="*50)
    print(paper.title)
    print(paper.source)