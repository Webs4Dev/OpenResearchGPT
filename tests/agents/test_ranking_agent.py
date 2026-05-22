from backend.retrieval.manager import retrieve_all
from backend.agents.ranking_agent import rank_paper

query="multi agent memory systems"

papers=retrieve_all(query,2)

for paper in papers[:3]:
    result=rank_paper(query,paper)
    print("="*50)
    print(result)