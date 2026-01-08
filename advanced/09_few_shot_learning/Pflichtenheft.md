# Pflichtenheft: Few-Shot Learning

## Expected Functionality
Teach models new tasks using examples (few-shot learning) with Ollama.

## Input
- `text` (str): Text to process
- `examples` (list): List of input/output examples
- `task` (str): Task description
- `model` (str, optional): Model to use

## Expected Output
```
=== Few-Shot Learning Demo ===
Test 1: Few-Shot Classification
Input: This is amazing!
Classification: Positive
```

## Tests
### Test 1: Classification
**Input:** Examples + new text
**Expected Output:** Correct classification

## Dependencies
```
ollama>=0.1.0
```

## Usage
```bash
python script.py
```
