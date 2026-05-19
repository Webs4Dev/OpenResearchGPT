import urllib.request
import arxiv
from backend.schemas.paper import Paper

opener = urllib.request.build_opener()
opener.addheaders = [
    ("User-Agent", "OpenResearchGPT/1.0 (devshah030206@gmail.com)")
]
urllib.request.install_opener(opener)

client = arxiv.Client(
    num_retries=2,
    delay_seconds=3,
    page_size=5
)

def search_papers(query: str, max_results: int):

    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    papers=[]

    try:
        for paper in client.results(search):

            papers.append(
                Paper(
                    title=paper.title,
                    summary=paper.summary,   # fixed
                    authors=[a.name for a in paper.authors],
                    published_year=paper.published.year,
                    url=paper.pdf_url,
                    source="arxiv"
                )
            )

    except Exception as e:
        print(f"Error: {e}")

    return papers