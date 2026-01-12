#!/usr/bin/env python3
"""Data Extractor Script - Extract structured data from text using Ollama LLM."""

import ollama

def extract_entities(text, entity_types, model="llama3"):
    """Extract specific entities from text."""
    prompt = f"Extract the following from this text: {', '.join(entity_types)}\n\nText: {text}\n\nProvide as a list."
    try:
        response = ollama.chat(model=model, messages=[{'role': 'user', 'content': prompt}])
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def extract_dates(text, model="llama3"):
    """Extract all dates from text."""
    prompt = f"Extract all dates from this text:\n\n{text}"
    try:
        response = ollama.chat(model=model, messages=[{'role': 'user', 'content': prompt}])
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    try:
        print(extract_dates("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
