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
    try:
        print(create_assistant("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
