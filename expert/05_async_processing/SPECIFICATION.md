# Pflichtenheft: Async Processing

## Expected Functionality
Implements asynchronous/concurrent processing for multiple Ollama requests.

## Input
- `prompts` (list): List of prompts
- `model` (str, optional): Model to use

## Expected Output
```
=== Async Processing Demo ===
Sequential Processing:
Time: 10.50s

Async Processing:
Time: 4.20s
Speedup: 2.50x
```

## Tests
### Test 1: Concurrent Processing
**Input:** Multiple prompts
**Expected Output:** Faster total time

## Dependencies
```
ollama>=0.1.0
```

## Usage
```bash
python script.py
```

## Learning Objectives
- Implement async patterns
- Concurrent API calls
- Optimize throughput
