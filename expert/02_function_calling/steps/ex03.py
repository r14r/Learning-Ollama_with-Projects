#!/usr/bin/env python3
"""Function Calling Script - Implement function/tool calling with Ollama."""

import ollama
import json

def get_weather(location):
    """Simulate weather API."""
    return f"Weather in {location}: Sunny, 22°C"

def calculate(operation, a, b):
    """Perform calculation."""
    ops = {'+': a+b, '-': a-b, '*': a*b, '/': a/b if b != 0 else "Error"}
    return ops.get(operation, "Unknown operation")

def main():
    try:
        print(get_weather("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
