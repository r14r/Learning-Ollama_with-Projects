#!/usr/bin/env python3
"""JSON Mode Script - Get structured JSON responses from Ollama."""

import ollama
import json

def get_json_response(prompt, model="llama3"):
    """Get structured JSON response."""
    full_prompt = f"{prompt}\n\nRespond with valid JSON only."
    
    try:
        response = ollama.generate(model=model, prompt=full_prompt)
        return response['response']
    except Exception as e:
        return f"Error: {str(e)}"

def extract_as_json(text, schema, model="llama3"):
    """Extract information as JSON with schema."""
    prompt = f"""Extract information from this text as JSON following this schema:
{json.dumps(schema, indent=2)}

Text: {text}

JSON output:"""
    
    try:
        response = ollama.generate(model=model, prompt=prompt)
        return response['response']
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    try:
        print(get_json_response("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
