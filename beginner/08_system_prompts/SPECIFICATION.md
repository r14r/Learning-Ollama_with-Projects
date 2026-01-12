# Pflichtenheft: System Prompts

## Expected Functionality
This script demonstrates how to use system prompts to control and customize LLM behavior. System prompts set the context, personality, and response style of the model before user interaction begins.

## Input
- **Function parameters**:
  - `user_message` (str): User's message
  - `system_prompt` (str): System prompt defining model behavior
  - `model` (str, optional, default: "llama3"): Name of the Ollama model to use

## Expected Output
```
=== System Prompts Demo ===

Test 1: Helpful Assistant
================================================================================
System: You are a helpful assistant that provides clear, concise answers.
User: What is Python?
Assistant: Python is a high-level programming language known for its simplicity and readability.

Test 2: Pirate Personality
================================================================================
System: You are a pirate who speaks in pirate slang. Use 'arrr' and pirate vocabulary.
User: Tell me about programming.
Pirate: Arrr, programmin' be the art of tellin' these digital contraptions what to do, matey!

Test 3: Code Expert
================================================================================
System: You are a Python expert. Always provide code examples and best practices.
User: How do I read a file?
Expert: Here's the best way to read a file in Python:

with open('file.txt', 'r') as f:
    content = f.read()
```

## Tests

### Test 1: Helpful Assistant
**Input:** System prompt for helpful behavior  
**Expected Output:** Clear, professional response

### Test 2: Personality Change
**Input:** Pirate personality system prompt  
**Expected Output:** Response with pirate slang and vocabulary

### Test 3: Domain Expert
**Input:** Expert system prompt with code request  
**Expected Output:** Response with code examples

### Test 4: Translator
**Input:** System prompt to translate to Spanish  
**Expected Output:** Spanish translation of user input

### Test 5: Format Control
**Input:** System prompt for structured/numbered responses  
**Expected Output:** Response in numbered format

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
- Understand the role of system prompts
- Control model personality and behavior
- Create custom AI assistants
- Structure response formats
- Apply system prompts to different use cases
- Build reusable assistant factories
