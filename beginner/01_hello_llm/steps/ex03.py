#!/usr/bin/env python3
"""
Hello LLM Script
A simple script that demonstrates basic interaction with Ollama LLM.
"""

import ollama

def greet_llm(model="llama3"):
    """
    Send a simple greeting to the LLM and get a response.
    
    Args:
        model (str): Name of the Ollama model to use (default: "llama3")
    
    Returns:
        str: The LLM's response
    """
    try:
        response = ollama.chat(
            model=model,
            messages=[
                {
                    'role': 'user',
                    'content': 'Hello! Please introduce yourself in one sentence.'
                }
            ]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def ask_question(question, model="llama3"):
    """
    Ask the LLM a question and get a response.
    
    Args:
        question (str): Question to ask
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
                    'content': question
                }
            ]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    try:
        print(greet_llm())
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
