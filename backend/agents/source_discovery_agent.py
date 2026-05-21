from backend.utils.source_config import RESEARCH_SOURCES


def generate_search_queries(user_query: str) -> list[str]:
    """
    Generate targeted search queries for research sources.
    """
    queries = []

    for source in RESEARCH_SOURCES:
        queries.append(
            f"{user_query} {source}"
        )

    return queries