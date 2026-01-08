# Pflichtenheft: Conversation History

## Expected Functionality
This script demonstrates how to maintain conversation context and history with Ollama. It shows why context matters and how to build a conversation manager that tracks message history.

## Input
- **Class parameters**:
  - `model` (str, optional, default: "llama3"): Name of the Ollama model to use
  - `system_prompt` (str, optional): System prompt for the conversation
- **Method parameters**:
  - `user_message` (str): User's message

## Expected Output
```
=== Conversation History Demo ===

User: What is 5 + 3?
Assistant: 5 + 3 equals 8.

User: Now multiply that by 2
Assistant: 8 multiplied by 2 equals 16.

User: And subtract 4 from the result
Assistant: 16 minus 4 equals 12.

================================================================================
Conversation History:
================================================================================
1. Role: system
   Content: You are a helpful math tutor.

2. Role: user
   Content: What is 5 + 3?

3. Role: assistant
   Content: 5 + 3 equals 8.
...
```

## Tests

### Test 1: Multi-turn Conversation
**Input:** Sequential messages referencing previous context  
**Expected Output:** Coherent responses that understand context

### Test 2: Context Reference
**Input:** "Now multiply that by 2" (after "What is 5 + 3?")  
**Expected Output:** Response referencing 8, the previous answer

### Test 3: Without Context
**Input:** "What is its capital?" without prior context  
**Expected Output:** Unclear or generic response

### Test 4: With Context
**Input:** "What is its capital?" after discussing France  
**Expected Output:** "Paris" or similar specific answer

### Test 5: History Management
**Input:** `conv.get_history()`  
**Expected Output:** List of all messages in order

### Test 6: Clear History
**Input:** `conv.clear_history()` then check history  
**Expected Output:** Only system message remains (if set)

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
- Understand conversation context importance
- Build a conversation manager class
- Track message history
- Handle multi-turn conversations
- Compare with-context vs without-context responses
- Manage conversation state
