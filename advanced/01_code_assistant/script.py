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
    """Main function to demonstrate code assistant features."""
    print("=== Code Assistant Demo ===\n")
    
    # Test 1: Generate code
    print("Test 1: Generate Code")
    print("=" * 80)
    description = "calculate the factorial of a number using recursion"
    print(f"Task: {description}\n")
    code = generate_code(description)
    print("Generated Code:")
    print(code)
    print()
    
    # Test 2: Explain code
    print("\nTest 2: Explain Code")
    print("=" * 80)
    sample_code = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
"""
    print(f"Code:{sample_code}")
    explanation = explain_code(sample_code)
    print(f"Explanation:\n{explanation}")
    print()
    
    # Test 3: Fix code
    print("\nTest 3: Fix Code")
    print("=" * 80)
    buggy_code = """
def divide(a, b):
    return a / b
"""
    error = "ZeroDivisionError when b is 0"
    print(f"Buggy Code:{buggy_code}")
    print(f"Error: {error}\n")
    fixed = fix_code(buggy_code, error)
    print(f"Fixed Code:\n{fixed}")
    print()
    
    # Test 4: Review code
    print("\nTest 4: Review Code")
    print("=" * 80)
    code_to_review = """
def process_list(lst):
    result = []
    for i in range(len(lst)):
        result.append(lst[i] * 2)
    return result
"""
    print(f"Code to Review:{code_to_review}")
    review = review_code(code_to_review)
    print(f"Review:\n{review}")


if __name__ == "__main__":
    main()
