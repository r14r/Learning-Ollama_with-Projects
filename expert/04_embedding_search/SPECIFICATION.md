# Pflichtenheft: Embedding Search

## Expected Functionality
Implements semantic search using Ollama embeddings and cosine similarity.

## Input
- `documents` (list): Documents to search
- `query` (str): Search query
- `model` (str, optional): Model for embeddings

## Expected Output
```
=== Embedding Search Demo ===
Query: programming languages
Top results:
  1. Python is a programming language
  2. Machine learning uses Python
```

## Tests
### Test 1: Semantic Search
**Input:** Query for similar documents
**Expected Output:** Most relevant documents

## Dependencies
```
ollama>=0.1.0
```

## Usage
```bash
python script.py
```

## Learning Objectives
- Use Ollama embeddings
- Implement semantic search
- Calculate similarity
