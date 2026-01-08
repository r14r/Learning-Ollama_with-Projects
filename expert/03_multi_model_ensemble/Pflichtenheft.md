# Pflichtenheft: Multi-Model Ensemble

## Expected Functionality
Uses multiple Ollama models together for consensus and comparison.

## Input
- `models` (list): List of model names
- `prompt` (str): Query for models

## Expected Output
```
=== Multi-Model Ensemble Demo ===
Individual Responses:
llama3: Paris is the capital...
Consensus Answer: Paris
```

## Tests
### Test 1: Query Multiple Models
**Input:** Question to ensemble
**Expected Output:** Responses from all models

## Dependencies
```
ollama>=0.1.0
```

## Usage
```bash
python script.py
```

## Learning Objectives
- Use multiple models
- Synthesize responses
- Build ensemble systems
