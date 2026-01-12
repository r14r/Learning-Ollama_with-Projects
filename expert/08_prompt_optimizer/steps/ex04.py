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
    print("=== Prompt Optimizer Demo ===\n")
    
    original = "Translate to French"
    goal = "Accurate French translation with context awareness"
    
    print(f"Original Prompt: {original}")
    print(f"Goal: {goal}\n")
    
    optimized = optimize_prompt(original, goal)
    print(f"Optimized Prompt:\n{optimized}\n")
    
    test_input = "Hello, how are you?"
    
    print(f"Testing with: {test_input}\n")
    print("Original result:")
    print(test_prompt(original, test_input)[:100] + "...\n")
    
    print("Optimized result:")
    print(test_prompt(optimized, test_input)[:100] + "...")

def main():
    print("Step 4: Kernbausteine geladen.")

if __name__ == "__main__":
    main()
