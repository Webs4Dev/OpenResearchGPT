import arxiv
import time 

client = arxiv.Client(
    num_retries=5,
    delay_seconds=5,  
)

def search_papers(query:str,max_results:int):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    results = []
    try:
        for paper in client.results(search):
            results.append({
                "title": paper.title,
                "summary": paper.summary,
                "authors": [a.name for a in paper.authors],
                "published":paper.published,
                "pdf_url": paper.pdf_url,
            })

            time.sleep(1)

    except Exception as e:
        print(f"Error: {e}")

    return results