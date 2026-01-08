# Pflichtenheft: Chat with Context

## Expected Functionality
Context-aware chatbot that remembers conversation and uses provided context.

## Input
- `model` (str): Model to use
- `context_doc` (str): Background context
- `user_message` (str): User input

## Expected Output
```
=== Context-Aware Chatbot Demo ===
Bot: Hello! How can I help you?
User: What products do you sell?
Bot: We sell laptops and phones...
```

## Tests
### Test 1: Use Context
**Input:** Chatbot with product context
**Expected Output:** Answers use context

## Dependencies
```
ollama>=0.1.0
```

## Usage
```bash
python script.py
```
