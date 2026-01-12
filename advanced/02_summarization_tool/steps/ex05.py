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
    """Main function to demonstrate summarization."""
    print("=== Text Summarization Demo ===\n")
    
    sample_text = """
    Artificial Intelligence (AI) has transformed numerous industries in recent years. 
    Machine learning algorithms can now process vast amounts of data to identify patterns 
    and make predictions. Deep learning, a subset of machine learning, uses neural networks 
    with multiple layers to achieve remarkable results in image recognition, natural language 
    processing, and game playing. Companies are investing heavily in AI research and 
    development, leading to breakthroughs in autonomous vehicles, healthcare diagnostics, 
    and personalized recommendations. However, ethical concerns about AI bias, privacy, 
    and job displacement remain important challenges that society must address.
    """
    
    # Test 1: Short summary
    print("Test 1: Short Summary")
    print("=" * 80)
    print(f"Original Text:{sample_text}")
    summary = summarize_text(sample_text, "short")
    print(f"\nShort Summary:\n{summary}\n")
    
    # Test 2: Bullet points
    print("\nTest 2: Bullet Point Summary")
    print("=" * 80)
    bullets = summarize_bullets(sample_text, 3)
    print(f"Summary (3 points):\n{bullets}\n")
    
    # Test 3: Key points
    print("\nTest 3: Extract Key Points")
    print("=" * 80)
    key_points = extract_key_points(sample_text)
    print(f"Key Points:\n{key_points}\n")
    
    # Test 4: Audience-specific
    print("\nTest 4: Summary for Children")
    print("=" * 80)
    child_summary = summarize_for_audience(sample_text, "children aged 10-12")
    print(f"Summary:\n{child_summary}")

def main():
    try:
        print(summarize_text("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
