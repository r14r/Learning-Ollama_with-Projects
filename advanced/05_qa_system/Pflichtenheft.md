# Pflichtenheft: QA System

## Expected Functionality
This script implements a question-answering system using Ollama LLM. It can answer questions with or without context, extract answers from documents, and verify answers against provided information.

## Input
- **Function parameters**:
  - `question` (str): Question to answer
  - `context` (str, optional): Context information
  - `document` (str, optional): Document text
  - `answer` (str): Proposed answer to verify
  - `model` (str, optional, default: "llama3"): Model to use

## Expected Output
```
=== Question-Answering System Demo ===

Test 1: Answer with Context
Context: Python was created by Guido van Rossum...

Question: When was Python first released?
Answer: Python was first released in 1991.

Test 2: Multiple Questions from Document
Q: Who created Python?
A: Guido van Rossum created Python.

Test 3: Verify Answer
Question: When was Python created?
Proposed Answer: 1991
Verification: Yes, the answer is correct...
```

## Tests

### Test 1: Simple Question
**Input:** `answer_question("What is 2+2?")`  
**Expected Output:** "4" or "The answer is 4"

### Test 2: Question with Context
**Input:** `answer_question("Who is the author?", "Book by John Smith")`  
**Expected Output:** Answer mentioning John Smith

### Test 3: Extract from Document
**Input:** `answer_from_document(question, document)`  
**Expected Output:** Answer based on document content

### Test 4: Verify Correct Answer
**Input:** `verify_answer("Who?", "John", "John is the author")`  
**Expected Output:** Confirmation answer is correct

## Dependencies
```
ollama>=0.1.0
```

## Prerequisites
- Ollama must be installed and running
- At least one model must be pulled (e.g., `ollama pull llama3`)

## Usage
```bash
python script.py
```

## Learning Objectives
- Build question-answering systems
- Use context effectively
- Extract information from documents
- Verify answers against sources
- Implement RAG-lite patterns
