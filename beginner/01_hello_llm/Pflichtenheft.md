# Pflichtenheft: Hello LLM

## Expected Functionality
This script demonstrates the most basic interaction with an Ollama LLM. It sends simple messages to the model and receives responses, introducing users to the fundamental chat interface pattern.

## Input
- **Function parameters**:
  - `model` (str, optional, default: "llama3"): Name of the Ollama model to use
  - `question` (str): Question or message to send to the LLM

## Expected Output
```
=== Hello LLM Demo ===

Test 1: Simple Greeting
LLM: I'm Llama 3, a large language model developed by Meta AI.

Test 2: Simple Question
Question: What is 2 + 2?
LLM: The answer is 4.

Test 3: Fun Fact
LLM: Python was named after the British comedy group Monty Python, not the snake!
```

## Tests

### Test 1: Simple Greeting
**Input:** `greet_llm()`  
**Expected Output:** A response string introducing the LLM (content varies by model)

### Test 2: Basic Question
**Input:** `ask_question("What is 2 + 2?")`  
**Expected Output:** A response containing "4" or equivalent answer

### Test 3: Custom Question
**Input:** `ask_question("Tell me a fun fact about Python programming language in one sentence.")`  
**Expected Output:** A single sentence containing a fact about Python

### Test 4: Error Handling
**Input:** `greet_llm(model="nonexistent_model")`  
**Expected Output:** String starting with "Error:" describing the issue

## Dependencies
```
ollama>=0.1.0
```

## Prerequisites
- Ollama must be installed and running
- At least one model must be pulled (e.g., `ollama pull llama3`)

## Usage
```bash
# Ensure Ollama is running and a model is available
ollama list

# Run the script
python script.py
```

## Learning Objectives
- Understand basic Ollama SDK structure
- Learn the chat interface pattern
- Handle messages and responses
- Basic error handling
