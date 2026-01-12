#!/usr/bin/env python3
"""
Simple Chat Script
A simple interactive chat interface with an Ollama LLM.
"""

import ollama

def chat_once(message, model="llama3"):
    """
    Send a single message to the LLM and get a response.
    
    Args:
        message (str): User message
        model (str): Name of the Ollama model to use
    
    Returns:
        str: The LLM's response
    """
    try:
        response = ollama.chat(
            model=model,
            messages=[
                {
                    'role': 'user',
                    'content': message
                }
            ]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def chat_interactive(model="llama3", max_turns=5):
    """
    Run an interactive chat session with the LLM.
    
    Args:
        model (str): Name of the Ollama model to use
        max_turns (int): Maximum number of chat turns
    
    Returns:
        list: List of (user_message, llm_response) tuples
    """
    conversation = []
    print(f"\n=== Interactive Chat with {model} ===")
    print(f"(You have {max_turns} messages. Type 'quit' to exit early)\n")
    
    for turn in range(max_turns):
        user_input = input(f"You: ").strip()
        
        if user_input.lower() == 'quit':
            print("Ending chat session.")
            break
        
        if not user_input:
            print("Please enter a message.\n")
            continue
        
        response = chat_once(user_input, model)
        print(f"LLM: {response}\n")
        
        conversation.append((user_input, response))
    
    return conversation

def demo_chat(model="llama3"):
    """
    Demonstrate chat with predefined messages.
    
    Args:
        model (str): Name of the Ollama model to use
    """
    messages = [
        "Hi there!",
        "What can you help me with?",
        "Tell me a joke."
    ]
    
    print(f"\n=== Demo Chat with {model} ===\n")
    
    for msg in messages:
        print(f"You: {msg}")
        response = chat_once(msg, model)
        print(f"LLM: {response}\n")

def main():
    """Main function to demonstrate simple chat."""
    import sys
    
    # Run demo chat
    demo_chat()
    
    # Check if we're in an interactive environment
    if sys.stdin.isatty():
        # Run interactive chat
        try:
            chat_interactive()
        except KeyboardInterrupt:
            print("\n\nChat interrupted by user.")
    else:
        print("\n(Skipping interactive chat in non-interactive mode)")

def main():
    try:
        print(chat_once("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
