# Advanced Beekeeping RAG System

## Overview

This project implements a Retrieval-Augmented Generation (RAG) pipeline for answering domain-specific questions related to Advanced Beekeeping Techniques.

The system ingests a knowledge document, generates vector embeddings, stores them in a FAISS vector database, retrieves relevant context for user queries, and generates accurate answers using a Large Language Model (LLM).

This project was developed as part of the Edxso AI Engineer Intern Assignment.


async video walkthrough : https://drive.google.com/file/d/1AYL9jLRDuIVpCyJCnbucaZv7aZMPZnTX/view?usp=drive_link

---

## Features

- Document Ingestion
- Text Chunking
- Embedding Generation
- FAISS Vector Database
- Context Retrieval
- Question Answering
- Evaluation Framework
- Semantic Similarity Analysis

---

## Tech Stack

### Frameworks & Libraries

- Python
- LangChain
- HuggingFace Embeddings
- Sentence Transformers
- FAISS
- Google Gemini API
- Scikit-Learn

---

## Project Architecture

```text
Knowledge Document
        │
        ▼
 Document Loader
        │
        ▼
 Text Splitter
        │
        ▼
 Embedding Model
        │
        ▼
   FAISS Index
        │
        ▼
   Retriever
        │
        ▼
      LLM
        │
        ▼
 Generated Answer
```

---

## Dataset

Domain: Advanced Beekeeping Techniques

Document Topics:

- Hive Winterization
- Internal Temperature Management
- Condensation Control
- Entrance Reducers
- Colony Protection

---

## Run RAG Pipeline

```bash
py main.py
```

Example Questions:

```text
What is the minimum internal temperature for a Langstroth Hive in winter?

Why are entrance reducers used?

How do beekeepers control condensation?
```

---

## Evaluation

Run:

```bash
py -m src.evaluate
```

The evaluation module compares generated answers against expected answers using:

- Semantic Similarity
- Keyword Overlap

---

## Sample Results

| Question | Status |
|-----------|---------|
| Minimum Hive Temperature | Correct |
| Purpose of Entrance Reducers | Correct |
| Condensation Control Method | Correct |

---

## Learning Outcomes

This project demonstrates:

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Embedding Models
- Context-Aware Question Answering
- AI Evaluation Techniques
- End-to-End LLM Application Development

---

## Future Improvements

- Multi-document support
- Hybrid Search
- Reranking
- Advanced Evaluation Metrics
- Streamlit User Interface
- Production Deployment

---

## Author

Vidya Bag

AI Engineer Intern Assignment Submission
