# Pflichtenheft: Data Extractor

## Expected Functionality
Extract structured data from unstructured text using Ollama LLM.

## Input
- `text` (str): Text to extract from
- `entity_types` (list): Types of entities to extract
- `model` (str, optional): Model to use

## Expected Output
```
=== Data Extractor Demo ===
Test 1: Extract Entities
Entities: Names: John Smith, Locations: New York
```

## Tests
### Test 1: Extract Names
**Input:** `extract_entities(text, ["names"])`
**Expected Output:** List of names

## Dependencies
```
ollama>=0.1.0
```

## Usage
```bash
python script.py
```
