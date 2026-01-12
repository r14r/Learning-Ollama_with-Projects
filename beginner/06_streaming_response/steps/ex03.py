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

def main():
    try:
        print(stream_response("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
