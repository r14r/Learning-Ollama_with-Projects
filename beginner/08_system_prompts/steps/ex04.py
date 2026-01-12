#!/usr/bin/env python3
"""
System Prompts Script
Demonstrates how to use system prompts to control model behavior.
"""

import ollama

def chat_with_system_prompt(user_message, system_prompt, model="llama3"):
    """
    Send a message with a system prompt.
    
    Args:
        user_message (str): User's message
        system_prompt (str): System prompt defining model behavior
        model (str): Name of the Ollama model to use
    
    Returns:
        str: Model's response
    """
    try:
        response = ollama.chat(
            model=model,
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_message}
            ]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def create_assistant(system_prompt, model="llama3"):
    """
    Create an assistant function with a specific system prompt.
    
    Args:
        system_prompt (str): System prompt defining assistant behavior
        model (str): Name of the Ollama model to use
    
    Returns:
        function: Function that takes user messages
    """
    def assistant(user_message):
        return chat_with_system_prompt(user_message, system_prompt, model)
    return assistant

def main():
    """Main function to demonstrate system prompts."""
    print("=== System Prompts Demo ===\n")
    
    # Test 1: Helpful assistant
    print("Test 1: Helpful Assistant")
    print("=" * 80)
    system_prompt = "You are a helpful assistant that provides clear, concise answers."
    response = chat_with_system_prompt(
        "What is Python?",
        system_prompt
    )
    print(f"System: {system_prompt}")
    print(f"User: What is Python?")
    print(f"Assistant: {response}\n")
    
    # Test 2: Pirate personality
    print("Test 2: Pirate Personality")
    print("=" * 80)
    system_prompt = "You are a pirate who speaks in pirate slang. Use 'arrr' and pirate vocabulary."
    response = chat_with_system_prompt(
        "Tell me about programming.",
        system_prompt
    )
    print(f"System: {system_prompt}")
    print(f"User: Tell me about programming.")
    print(f"Pirate: {response}\n")
    
    # Test 3: Code expert
    print("Test 3: Code Expert")
    print("=" * 80)
    system_prompt = "You are a Python expert. Always provide code examples and best practices."
    response = chat_with_system_prompt(
        "How do I read a file?",
        system_prompt
    )
    print(f"System: {system_prompt}")
    print(f"User: How do I read a file?")
    print(f"Expert: {response}\n")
    
    # Test 4: Using the assistant factory
    print("Test 4: Custom Assistant Factory")
    print("=" * 80)
    translator = create_assistant(
        "You are a translator. Translate all user input to Spanish."
    )
    response = translator("Hello, how are you?")
    print(f"Translator: {response}\n")
    
    # Test 5: JSON responder
    print("Test 5: Structured Response")
    print("=" * 80)
    system_prompt = "Always respond in a structured format with numbered points."
    response = chat_with_system_prompt(
        "Give me 3 tips for learning Python.",
        system_prompt
    )
    print(f"System: {system_prompt}")
    print(f"User: Give me 3 tips for learning Python.")
    print(f"Assistant: {response}")

def main():
    try:
        print(create_assistant("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
