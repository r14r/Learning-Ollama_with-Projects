# Pflichtenheft: Streaming Response

## Expected Functionality
This script demonstrates how to stream responses from Ollama in real-time, providing immediate feedback to users as the model generates text. It shows both chat and generation streaming modes.

## Input
- **Function parameters**:
  - `prompt` (str): User prompt or text to process
  - `model` (str, optional, default: "llama3"): Name of the Ollama model to use

## Expected Output
```
=== Streaming Response Demo ===

Test 1: Streaming Chat Response
------------------------------------------------------------
Code flows like water,
Logic branches, loops return,
Functions find their way.

Test 2: Streaming Text Generation
------------------------------------------------------------
bright and full of possibilities...

Test 3: Comparison
============================================================

--- Non-Streaming Response ---
1. One - The first number
2. Two - The second number
...
(Received after 2.34 seconds)

--- Streaming Response ---
1. One - The first number
2. Two - The second number
...
(Completed in 2.35 seconds)
```

## Tests

### Test 1: Stream Chat Response
**Input:** `stream_response("Say hello")`  
**Expected Output:** Streaming output printed character by character, returns complete text

### Test 2: Stream Generate
**Input:** `stream_generate("Once upon a time")`  
**Expected Output:** Streaming generation output, returns complete text

### Test 3: Verify Streaming Works
**Input:** `stream_response("Count to 3")`  
**Expected Output:** Text appears progressively (observable in real-time)

### Test 4: Long Response
**Input:** `stream_response("Write a short story")`  
**Expected Output:** Story text streams in real-time

### Test 5: Error Handling
**Input:** `stream_response("test", model="invalid")`  
**Expected Output:** Error message displayed

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
- Understand streaming vs non-streaming responses
- Use stream=True parameter
- Handle streaming chunks
- Implement real-time output display
- Compare user experience between modes
- Manage streaming in both chat and generate APIs
