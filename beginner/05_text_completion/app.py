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


def complete_code(code_snippet, model="llama3"):
    """
    Complete a code snippet.
    
    Args:
        code_snippet (str): Partial code
        model (str): Name of the Ollama model to use
    
    Returns:
        str: Completed code
    """
    prompt = f"Complete this code:\n\n{code_snippet}"
    return complete_text(prompt, model)


def main():
    """Main function to demonstrate text completion."""
    print("=== Text Completion Demo ===\n")
    
    # Test 1: Simple sentence completion
    print("Test 1: Sentence Completion")
    prompt = "The quick brown fox"
    result = complete_text(prompt)
    print(f"Prompt: {prompt}")
    print(f"Completion: {result}\n")
    
    # Test 2: Story completion
    print("Test 2: Story Completion")
    story_start = "Once upon a time, in a small village, there lived a young programmer who discovered"
    result = complete_story(story_start)
    print(f"Story Beginning: {story_start}")
    print(f"Completion: {result}\n")
    
    # Test 3: Code completion
    print("Test 3: Code Completion")
    code = "def fibonacci(n):\n    if n <= 1:\n        return n"
    result = complete_code(code)
    print(f"Code Snippet:\n{code}")
    print(f"\nCompletion:\n{result}")


if __name__ == "__main__":
    main()
