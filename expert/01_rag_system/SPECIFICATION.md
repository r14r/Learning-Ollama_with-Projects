# Pflichtenheft: RAG System

## Expected Functionality
Implements Retrieval Augmented Generation (RAG) pattern with Ollama for answering questions based on document retrieval.

## Input
- `documents` (list): Knowledge base documents
- `query` (str): User question
- `model` (str, optional): Model to use

## Expected Output
```
=== RAG System Demo ===
Question: Who created Python?
Answer: Python was created by Guido van Rossum.
```

## Tests
### Test 1: Retrieve and Answer
**Input:** Question about documents
**Expected Output:** Accurate answer from context

## Dependencies
```
ollama>=0.1.0
```

## Usage
```bash
python script.py
```

## Learning Objectives
- Implement RAG pattern
- Combine retrieval with generation
- Build knowledge-based systems
