# Pflichtenheft: Text Completion

## Expected Functionality
This script demonstrates text completion using Ollama's generate API. It shows how to complete sentences, stories, and code snippets.

## Input
- **Function parameters**:
  - `prompt` (str): Text to complete
  - `model` (str, optional, default: "llama3"): Name of the Ollama model to use
  - `max_tokens` (int, optional, default: 100): Maximum response length

## Expected Output
```
=== Text Completion Demo ===

Test 1: Sentence Completion
Prompt: The quick brown fox
Completion: jumps over the lazy dog. This classic sentence is often used...

Test 2: Story Completion
Story Beginning: Once upon a time, in a small village, there lived a young programmer who discovered
Completion: a magical algorithm that could solve any problem. One day...

Test 3: Code Completion
Code Snippet:
def fibonacci(n):
    if n <= 1:
        return n

Completion:
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

## Tests

### Test 1: Simple Completion
**Input:** `complete_text("The capital of France is")`  
**Expected Output:** Text completing the sentence (should mention Paris)

### Test 2: Story Completion
**Input:** `complete_story("Once upon a time")`  
**Expected Output:** Continuation of the story

### Test 3: Code Completion
**Input:** `complete_code("def add(a, b):")`  
**Expected Output:** Code completion with return statement

### Test 4: Multi-line Prompt
**Input:** `complete_text("Line 1\nLine 2\nLine 3")`  
**Expected Output:** Continuation following the pattern

### Test 5: Empty Prompt
**Input:** `complete_text("")`  
**Expected Output:** Generated text starting from scratch

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
- Use ollama.generate() for text completion
- Understand the difference between chat and generate APIs
- Apply completion to different domains (text, stories, code)
- Work with prompt engineering
