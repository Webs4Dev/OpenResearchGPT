from backend.retrieval.manager_retriever import retrieve_all

papers = retrieve_all(
    query="LLM Fine Tuning using LoRa",
    max_results=2
)

for i,paper in enumerate(papers):

    print("="*50)
    print(f"{i+1}. {paper.title}")
    print(paper.source)