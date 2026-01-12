#!/usr/bin/env python3
"""
Text Completion Script
Demonstrates text completion using Ollama.
"""

import ollama

def complete_text(prompt, model="llama3", max_tokens=100):
    """
    Complete a text prompt using the LLM.
    
    Args:
        prompt (str): Text to complete
        model (str): Name of the Ollama model to use
        max_tokens (int): Maximum tokens in response
    
    Returns:
        str: Completed text
    """
    try:
        response = ollama.generate(
            model=model,
            prompt=prompt
        )
        return response['response']
    except Exception as e:
        return f"Error: {str(e)}"

def complete_story(beginning, model="llama3"):
    """
    Complete a story beginning.
    
    Args:
        beginning (str): Story beginning
        model (str): Name of the Ollama model to use
    
    Returns:
        str: Completed story
    """
    prompt = f"{beginning}\n\nContinue this story:"
    return complete_text(prompt, model)

def main():
    try:
        print(complete_text("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
