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

def generate_with_options(prompt, model="llama3", **options):
    """
    Generate text with custom options.
    
    Args:
        prompt (str): User prompt
        model (str): Name of the Ollama model to use
        **options: Additional model options
    
    Returns:
        str: Generated response
    """
    try:
        response = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}],
            options=options
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    """Main function to demonstrate temperature control."""
    print("=== Temperature Control Demo ===\n")
    
    # Test 1: Low temperature (more focused)
    print("Test 1: Low Temperature (0.0) - More Focused and Deterministic")
    print("=" * 80)
    prompt = "What is 2+2?"
    response = generate_with_temperature(prompt, 0.0)
    print(f"Prompt: {prompt}")
    print(f"Response: {response}\n")
    
    # Test 2: High temperature (more creative)
    print("Test 2: High Temperature (1.5) - More Creative and Random")
    print("=" * 80)
    prompt = "Write a creative name for a space cat."
    response = generate_with_temperature(prompt, 1.5)
    print(f"Prompt: {prompt}")
    print(f"Response: {response}\n")
    
    # Test 3: Compare temperatures
    print("Test 3: Temperature Comparison")
    print("=" * 80)
    compare_temperatures("Complete this: The ocean is")
    
    # Test 4: Multiple options
    print("\n\nTest 4: Multiple Options (Temperature + Top P)")
    print("=" * 80)
    response = generate_with_options(
        "Suggest a programming project idea.",
        temperature=0.7,
        top_p=0.9,
        top_k=40
    )
    print(f"Response: {response}")

def main():
    try:
        print(compare_temperatures("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
