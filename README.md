# OpenResearchGPT

OpenResearchGPT is an open-source multi-agent research discovery and analysis platform designed to help users find, understand, rank, and interact with research papers from multiple sources.

Instead of acting as a simple paper search tool, OpenResearchGPT aims to explain *why* papers are recommended, deeply analyze research content, and help users discover papers relevant to their own projects.

---

## Core Features

### Multi-Source Research Retrieval
Retrieve research papers from multiple sources:

- arXiv
- Semantic Scholar
- PubMed
- OpenAlex
- CrossRef
- Government research sites
- University repositories
- Other web sources

---

### Web Retrieval Agent

Discover and retrieve research papers from websites that do not provide Python libraries or APIs.

Examples:

- .gov research portals
- research lab websites
- university repositories
- organization publications

---

### Paper Ranking Agent

Rank papers using factors such as:

- semantic similarity
- recency
- citation count
- methodology match
- source quality
- project relevance

---

### Explanation Agent

Explain why a paper was selected.

Example:

Paper: Memory Architectures for LLM Agents

Why selected:

- Matches multi-agent memory systems
- Strong methodology overlap
- Recent publication
- High semantic similarity

---

### PDF Deep Dive Agent

Upload a paper and let the system:

- identify relevant sections
- highlight useful content
- explain difficult concepts
- answer questions
- connect paper ideas to your project

---

### Citation-Aware RAG

Interact with papers through conversational retrieval while preserving citations and context.

---

### Future Features

- Research gap detection
- Literature review generation
- Fine-tuned explainer model (LoRA)
- Personalized research memory
- Citation graph visualization
- Model evaluation pipeline
- Local model support
- PDF highlighting generation

---

## Project Architecture

```text
User Query
    ↓
Query Understanding Agent
    ↓
Retrieval Manager
        ↓
        ├── arXiv
        ├── Semantic Scholar
        ├── PubMed
        ├── OpenAlex
        ├── CrossRef
        └── Web Retrieval Agent
                    ↓
              Government sites
              University sites
              Research pages
    ↓
Ranking Agent
    ↓
Explanation Agent
    ↓
Results
```

PDF workflow:

```text
PDF Upload
    ↓
Parser
    ↓
Chunking
    ↓
Embeddings
    ↓
Project-Relevance Agent
    ↓
Highlighted Sections
    ↓
Q&A Agent
```

---

## Current Progress

- ✅ Day 1: Project setup
- ✅ Day 2: arXiv paper retrieval
- ✅ Day 3: Semantic Scholar retrieval
- ✅ Day 4: Retrieval manager and logging

---

## Tech Stack (Planned)

Backend:
- Python
- FastAPI
- LangGraph

AI:
- OpenAI API
- LoRA fine-tuning
- RAG

Database:
- ChromaDB

PDF Processing:
- PyMuPDF

Deployment:
- Docker

---

## Contributing

Contributions, ideas, and feature suggestions are welcome.
Future contribution guidelines will be added.

---

## License

MIT License