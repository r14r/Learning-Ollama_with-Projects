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

def extract_contact_info(text, model="llama3"):
    """Extract contact information."""
    prompt = f"Extract email addresses, phone numbers, and names from:\n\n{text}"
    try:
        response = ollama.chat(model=model, messages=[{'role': 'user', 'content': prompt}])
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("=== Data Extractor Demo ===\n")
    sample = "John Smith (john@email.com, 555-1234) will meet on Jan 15, 2024 in New York."
    
    print("Test 1: Extract Entities")
    entities = extract_entities(sample, ["names", "locations"])
    print(f"Text: {sample}")
    print(f"Entities: {entities}\n")
    
    print("Test 2: Extract Dates")
    dates = extract_dates(sample)
    print(f"Dates: {dates}\n")
    
    print("Test 3: Extract Contact Info")
    contact = extract_contact_info(sample)
    print(f"Contact Info: {contact}")

def main():
    try:
        print(extract_dates("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
