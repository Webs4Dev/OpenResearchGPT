from backend.agents.source_discovery_agent import generate_search_queries

queries = generate_search_queries("multi agent memory systems")
print("\nGenerated Queries:")

for query in queries:
    print(query)