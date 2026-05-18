from backend.schemas.paper import Paper
from semanticscholar import SemanticScholar
from dotenv import load_dotenv
import os
load_dotenv()

S2_API_KEY = os.getenv("S2_API_KEY")
sch = SemanticScholar(api_key=S2_API_KEY)

def search_papers(query: str, max_results: int):
    papers = []
    try:
        response = sch.search_paper(
            query=query,
            limit=max_results,
        )

        for paper in response.items:
            papers.append(Paper(
                title=paper.title,
                abstract=paper.abstract,
                authors=[a.name for a in paper.authors],
                published_year=paper.year,
                url=paper.url,
                source="semantic_scholar"
                ))
            
    except Exception as e:
        print(f"Error: {e}")

    return papers