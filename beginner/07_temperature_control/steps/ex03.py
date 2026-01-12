#!/usr/bin/env python3
"""
Temperature Control Script
Demonstrates how to control model behavior using temperature and other parameters.
"""

import ollama

def generate_with_temperature(prompt, temperature, model="llama3"):
    """
    Generate text with a specific temperature setting.
    
    Args:
        prompt (str): User prompt
        temperature (float): Temperature value (0.0 to 2.0)
        model (str): Name of the Ollama model to use
    
    Returns:
        str: Generated response
    """
    try:
        response = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}],
            options={'temperature': temperature}
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def compare_temperatures(prompt, model="llama3"):
    """
    Compare outputs at different temperature settings.
    
    Args:
        prompt (str): User prompt
        model (str): Name of the Ollama model to use
    """
    temperatures = [0.0, 0.5, 1.0, 1.5]
    
    print(f"Prompt: {prompt}\n")
    print("=" * 80)
    
    for temp in temperatures:
        print(f"\nTemperature: {temp}")
        print("-" * 80)
        response = generate_with_temperature(prompt, temp, model)
        print(response)

def main():
    try:
        print(compare_temperatures("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
