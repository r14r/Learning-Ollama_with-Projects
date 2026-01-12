# Pflichtenheft: JSON Mode

## Expected Functionality
Get structured JSON responses from Ollama LLM.

## Input
- `prompt` (str): Request for JSON
- `text` (str): Text to extract from
- `schema` (dict): JSON schema
- `model` (str, optional): Model to use

## Expected Output
```
=== JSON Mode Demo ===
Test 1: Person Information as JSON
JSON Output:
{"name": "John Smith", "age": 30, ...}
```

## Tests
### Test 1: Extract as JSON
**Input:** Text + schema
**Expected Output:** Valid JSON

## Dependencies
```
ollama>=0.1.0
```

## Usage
```bash
python script.py
```
