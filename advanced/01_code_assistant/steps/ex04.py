#!/usr/bin/env python3
"""
Code Assistant Script
An AI-powered code generation and assistance tool using Ollama.
"""

import ollama

def generate_code(description, language="Python", model="llama3"):
    """
    Generate code based on a description.
    
    Args:
        description (str): Description of what the code should do
        language (str): Programming language
        model (str): Model to use (llama3 by default, codellama recommended if available)
    
    Returns:
        str: Generated code
    """
    prompt = f"Write {language} code that: {description}\n\nProvide only the code, no explanations."
    
    try:
        response = ollama.generate(model=model, prompt=prompt)
        return response['response']
    except Exception as e:
        return f"Error: {str(e)}"

def explain_code(code, model="llama3"):
    """
    Explain what a piece of code does.
    
    Args:
        code (str): Code to explain
        model (str): Model to use
    
    Returns:
        str: Explanation
    """
    prompt = f"Explain what this code does:\n\n{code}"
    
    try:
        response = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def fix_code(code, error, model="llama3"):
    """
    Fix code given an error message.
    
    Args:
        code (str): Code with error
        error (str): Error message
        model (str): Model to use
    
    Returns:
        str: Fixed code
    """
    prompt = f"""Fix this code:

{code}

Error: {error}

Provide the corrected code only."""
    
    try:
        response = ollama.generate(model=model, prompt=prompt)
        return response['response']
    except Exception as e:
        return f"Error: {str(e)}"

def review_code(code, model="llama3"):
    """
    Review code and suggest improvements.
    
    Args:
        code (str): Code to review
        model (str): Model to use
    
    Returns:
        str: Review and suggestions
    """
    prompt = f"""Review this code and suggest improvements:

{code}

Provide:
1. What it does well
2. Potential issues
3. Suggested improvements"""
    
    try:
        response = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    try:
        print(generate_code("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
