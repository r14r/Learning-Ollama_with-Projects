#!/usr/bin/env python3
"""
Translation Service Script
Multi-language translation using Ollama LLM.
"""

import ollama

def translate(text, target_language, source_language="auto", model="llama3"):
    """
    Translate text to target language.
    
    Args:
        text (str): Text to translate
        target_language (str): Target language
        source_language (str): Source language (default: "auto")
        model (str): Model to use
    
    Returns:
        str: Translated text
    """
    if source_language == "auto":
        prompt = f"Translate this text to {target_language}:\n\n{text}"
    else:
        prompt = f"Translate this text from {source_language} to {target_language}:\n\n{text}"
    
    try:
        response = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def detect_language(text, model="llama3"):
    """
    Detect the language of text.
    
    Args:
        text (str): Text to analyze
        model (str): Model to use
    
    Returns:
        str: Detected language
    """
    prompt = f"What language is this text written in? Respond with just the language name.\n\nText: {text}"
    
    try:
        response = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    try:
        print(detect_language("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
