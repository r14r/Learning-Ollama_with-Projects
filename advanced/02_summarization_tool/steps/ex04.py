#!/usr/bin/env python3
"""
Summarization Tool Script
Text summarization using Ollama LLM.
"""

import ollama

def summarize_text(text, length="short", model="llama3"):
    """
    Summarize text with specified length.
    
    Args:
        text (str): Text to summarize
        length (str): "short", "medium", or "long"
        model (str): Model to use
    
    Returns:
        str: Summary
    """
    length_instructions = {
        "short": "in 1-2 sentences",
        "medium": "in 3-5 sentences",
        "long": "in 1-2 paragraphs"
    }
    
    instruction = length_instructions.get(length, "in 3-5 sentences")
    prompt = f"Summarize the following text {instruction}:\n\n{text}"
    
    try:
        response = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def summarize_bullets(text, num_points=5, model="llama3"):
    """
    Summarize text as bullet points.
    
    Args:
        text (str): Text to summarize
        num_points (int): Number of bullet points
        model (str): Model to use
    
    Returns:
        str: Summary in bullet points
    """
    prompt = f"Summarize the following text in {num_points} bullet points:\n\n{text}"
    
    try:
        response = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def extract_key_points(text, model="llama3"):
    """
    Extract key points from text.
    
    Args:
        text (str): Text to analyze
        model (str): Model to use
    
    Returns:
        str: Key points
    """
    prompt = f"""Extract the key points from this text:

{text}

List the main ideas and important information."""
    
    try:
        response = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def summarize_for_audience(text, audience, model="llama3"):
    """
    Summarize text for a specific audience.
    
    Args:
        text (str): Text to summarize
        audience (str): Target audience (e.g., "children", "experts")
        model (str): Model to use
    
    Returns:
        str: Audience-appropriate summary
    """
    prompt = f"Summarize this text for {audience}:\n\n{text}"
    
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
        print(summarize_text("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
