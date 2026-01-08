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
    """Main function to demonstrate LLM interaction."""
    print("=== Hello LLM Demo ===\n")
    
    # Test 1: Simple greeting
    print("Test 1: Simple Greeting")
    greeting = greet_llm()
    print(f"LLM: {greeting}\n")
    
    # Test 2: Ask a simple question
    print("Test 2: Simple Question")
    question = "What is 2 + 2?"
    answer = ask_question(question)
    print(f"Question: {question}")
    print(f"LLM: {answer}\n")
    
    # Test 3: Ask for a fun fact
    print("Test 3: Fun Fact")
    fact = ask_question("Tell me a fun fact about Python programming language in one sentence.")
    print(f"LLM: {fact}")


if __name__ == "__main__":
    main()
