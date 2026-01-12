# Pflichtenheft: Prompt Templates

## Expected Functionality
This script demonstrates how to create and use prompt templates with Ollama. Templates allow you to create reusable prompt structures that can be filled with different data, making your code more maintainable and flexible.

## Input
- **Function parameters**:
  - `template_str` (str): Template string with {variable} placeholders
  - `model` (str, optional, default: "llama3"): Name of the Ollama model to use
  - `**kwargs`: Variables to fill in the template

## Expected Output
```
=== Prompt Templates Demo ===

Template 1: Translation
Result: Hola, ¿cómo estás?

Template 2: Summarization
Result: Python is a high-level programming language created by Guido van Rossum in 1991. It emphasizes code readability and expressive syntax.

Template 3: Question with Context
Result: The Eiffel Tower was built in 1889.
```

## Tests

### Test 1: Translation Template
**Input:** 
```python
template = create_template("Translate to {language}: '{text}'")
use_template(template, language="French", text="Hello")
```
**Expected Output:** French translation of "Hello"

### Test 2: Summarization Template
**Input:** 
```python
template = create_template("Summarize in {num_sentences} sentences: {text}")
use_template(template, num_sentences="1", text="Long text...")
```
**Expected Output:** One-sentence summary

### Test 3: QA Template
**Input:** 
```python
template = create_template("Context: {context}\n\nQuestion: {question}")
use_template(template, context="...", question="...")
```
**Expected Output:** Answer based on context

### Test 4: Multiple Variables
**Input:** Template with 3+ variables filled correctly  
**Expected Output:** Properly formatted prompt and LLM response

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
- Create reusable prompt templates
- Use string formatting with variables
- Separate prompt structure from data
- Build maintainable prompting patterns
- Understand template-based programming
