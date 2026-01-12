# Pflichtenheft: Simple Chat

## Expected Functionality
This script demonstrates a simple chat interface with an Ollama LLM. It includes both a demo mode with predefined messages and an interactive mode where users can chat with the model in real-time.

## Input
- **Function parameters**:
  - `message` (str): User message to send
  - `model` (str, optional, default: "llama3"): Name of the Ollama model to use
  - `max_turns` (int, optional, default: 5): Maximum number of conversation turns
- **Interactive input**: User messages via stdin

## Expected Output
```
=== Demo Chat with llama3 ===

You: Hi there!
LLM: Hello! It's nice to meet you. How can I help you today?

You: What can you help me with?
LLM: I can help with a wide variety of tasks including answering questions, providing explanations, helping with writing, coding assistance, and more.

You: Tell me a joke.
LLM: Why don't scientists trust atoms? Because they make up everything!

=== Interactive Chat with llama3 ===
(You have 5 messages. Type 'quit' to exit early)

You: [user input]
LLM: [model response]
```

## Tests

### Test 1: Single Message
**Input:** `chat_once("Hello")`  
**Expected Output:** A greeting response from the LLM

### Test 2: Question
**Input:** `chat_once("What is the capital of France?")`  
**Expected Output:** Response containing "Paris"

### Test 3: Demo Chat
**Input:** `demo_chat()`  
**Expected Output:** Three exchanges with predefined messages

### Test 4: Error Handling
**Input:** `chat_once("Hello", model="invalid_model")`  
**Expected Output:** String starting with "Error:"

### Test 5: Interactive Chat
**Input:** `chat_interactive(max_turns=2)` with user inputs "Hello" and "Goodbye"  
**Expected Output:** List with 2 tuples of (user_message, llm_response)

## Dependencies
```
ollama>=0.1.0
```

## Prerequisites
- Ollama must be installed and running
- At least one model must be pulled (e.g., `ollama pull llama3`)

## Usage
```bash
# Run demo chat
python script.py

# For interactive chat, run in a terminal
python script.py
# Then type your messages when prompted
```

## Learning Objectives
- Build a simple chat interface
- Handle user input
- Display conversational output
- Manage interactive vs. non-interactive modes
- Structure multi-turn conversations
