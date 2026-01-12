# Pflichtenheft: Function Calling

## Expected Functionality
Implements function/tool calling patterns where LLM decides when to call functions.

## Input
- `user_request` (str): User's request
- `model` (str, optional): Model to use

## Expected Output
```
=== Function Calling Demo ===
Request: What's the weather in Paris?
Response: Function: get_weather
Result: Weather in Paris: Sunny, 22°C
```

## Tests
### Test 1: Call Function
**Input:** Request needing function
**Expected Output:** Function called with results

## Dependencies
```
ollama>=0.1.0
```

## Usage
```bash
python script.py
```

## Learning Objectives
- Implement tool use patterns
- Parse function calls from LLM
- Build agentic systems
