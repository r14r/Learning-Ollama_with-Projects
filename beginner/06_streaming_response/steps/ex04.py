#!/usr/bin/env python3
"""
Streaming Response Script
Demonstrates how to stream responses from Ollama for real-time output.
"""

import ollama
import sys

def stream_response(prompt, model="llama3"):
    """
    Stream a response from the LLM.
    
    Args:
        prompt (str): User prompt
        model (str): Name of the Ollama model to use
    
    Returns:
        str: Complete response text
    """
    full_response = ""
    
    try:
        stream = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}],
            stream=True
        )
        
        for chunk in stream:
            content = chunk['message']['content']
            print(content, end='', flush=True)
            full_response += content
        
        print()  # New line after streaming
        return full_response
        
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        print(error_msg)
        return error_msg

def stream_generate(prompt, model="llama3"):
    """
    Stream text generation response.
    
    Args:
        prompt (str): Text prompt
        model (str): Name of the Ollama model to use
    
    Returns:
        str: Complete generated text
    """
    full_response = ""
    
    try:
        stream = ollama.generate(
            model=model,
            prompt=prompt,
            stream=True
        )
        
        for chunk in stream:
            content = chunk['response']
            print(content, end='', flush=True)
            full_response += content
        
        print()  # New line after streaming
        return full_response
        
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        print(error_msg)
        return error_msg

def compare_streaming_vs_non_streaming(prompt, model="llama3"):
    """
    Compare streaming vs non-streaming responses.
    
    Args:
        prompt (str): User prompt
        model (str): Name of the Ollama model to use
    """
    print("\n--- Non-Streaming Response ---")
    import time
    start = time.time()
    
    response = ollama.chat(
        model=model,
        messages=[{'role': 'user', 'content': prompt}]
    )
    
    elapsed = time.time() - start
    print(response['message']['content'])
    print(f"\n(Received after {elapsed:.2f} seconds)\n")
    
    print("--- Streaming Response ---")
    start = time.time()
    stream_response(prompt, model)
    elapsed = time.time() - start
    print(f"(Completed in {elapsed:.2f} seconds)")

def main():
    """Main function to demonstrate streaming responses."""
    print("=== Streaming Response Demo ===\n")
    
    # Test 1: Simple streaming
    print("Test 1: Streaming Chat Response")
    print("-" * 60)
    stream_response("Write a haiku about programming.")
    print()
    
    # Test 2: Streaming generation
    print("\nTest 2: Streaming Text Generation")
    print("-" * 60)
    stream_generate("Complete this: The future of AI is")
    print()
    
    # Test 3: Compare streaming vs non-streaming
    print("\nTest 3: Comparison")
    print("=" * 60)
    compare_streaming_vs_non_streaming("Count from 1 to 5 with descriptions.")

def main():
    try:
        print(stream_response("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
