# Pflichtenheft: Code Assistant

## Expected Functionality
This script provides AI-powered code assistance including code generation, explanation, debugging, and review. It uses Ollama models (preferably CodeLlama) to help developers with various programming tasks.

## Input
- **Function parameters**:
  - `description` (str): Description of code to generate
  - `code` (str): Code to explain, fix, or review
  - `error` (str): Error message for debugging
  - `language` (str, optional, default: "Python"): Programming language
  - `model` (str, optional, default: "codellama"): Model to use

## Expected Output
```
=== Code Assistant Demo ===

Test 1: Generate Code
================================================================================
Task: calculate the factorial of a number using recursion

Generated Code:
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

Test 2: Explain Code
================================================================================
Code:
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

Explanation:
This function calculates the nth Fibonacci number using recursion...

Test 3: Fix Code
================================================================================
Buggy Code:
def divide(a, b):
    return a / b

Error: ZeroDivisionError when b is 0

Fixed Code:
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

## Tests

### Test 1: Generate Simple Function
**Input:** `generate_code("sort a list of numbers")`  
**Expected Output:** Code implementing a sorting function

### Test 2: Generate with Language
**Input:** `generate_code("hello world", language="JavaScript")`  
**Expected Output:** JavaScript code

### Test 3: Explain Code
**Input:** `explain_code("def add(a, b): return a + b")`  
**Expected Output:** Explanation of the addition function

### Test 4: Fix Syntax Error
**Input:** `fix_code("def func() print('hi')", "SyntaxError")`  
**Expected Output:** Fixed code with proper syntax

### Test 5: Code Review
**Input:** `review_code(code_sample)`  
**Expected Output:** Review with strengths, issues, and improvements

## Dependencies
```
ollama>=0.1.0
```

## Prerequisites
- Ollama must be installed and running
- At least one model must be pulled (e.g., `ollama pull llama3`)
- CodeLlama or similar code model recommended for best results: `ollama pull codellama`
  - If CodeLlama is not available, the scripts will work with llama3 as default
- Alternative: Use llama3 or another model by changing the model parameter

## Usage
```bash
# Pull code model (recommended)
ollama pull codellama

# Run the script
python script.py
```

## Learning Objectives
- Use LLMs for code generation
- Implement code explanation features
- Debug code with AI assistance
- Perform automated code reviews
- Work with code-specialized models
- Apply AI to software development workflows
