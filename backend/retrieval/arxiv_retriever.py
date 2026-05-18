import arxiv
from backend.schemas.paper import Paper 

client = arxiv.Client(
    num_retries=2,
    delay_seconds=3,
    page_size=10  
)

def search_papers(query:str,max_results:int):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    papers=[] 
    try:
        for paper in client.results(search):
            papers.append(Paper(
                title=paper.title,
                abstract= paper.summary,
                authors= [a.name for a in paper.authors],
                published_year=paper.published.year,
                url= paper.pdf_url,
                source="arxiv"
            ))

    except Exception as e:
        print(f"Error: {e}")

    return papers