#!/usr/bin/env python3
"""Prompt Optimizer - Optimize prompts for better results."""

import ollama

def optimize_prompt(original_prompt, goal, model="llama3"):
    """Optimize a prompt for better results."""
    meta_prompt = f"""Improve this prompt to better achieve the goal:

Original Prompt: {original_prompt}
Goal: {goal}

Provide an optimized prompt:"""
    
    try:
        response = ollama.generate(model=model, prompt=meta_prompt)
        return response['response']
    except Exception as e:
        return f"Error: {str(e)}"

def test_prompt(prompt, test_input, model="llama3"):
    """Test a prompt with input."""
    full_prompt = f"{prompt}\n\nInput: {test_input}"
    try:
        response = ollama.generate(model=model, prompt=full_prompt)
        return response['response']
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Step 3: Kernbausteine geladen.")

if __name__ == "__main__":
    main()
