#!/usr/bin/env python3
"""
Content Generator Script
Generate various types of content using Ollama LLM.
"""

import ollama

def generate_blog_post(topic, length="medium", model="llama3"):
    """Generate a blog post on a topic."""
    lengths = {"short": "300 words", "medium": "500 words", "long": "800 words"}
    word_count = lengths.get(length, "500 words")
    
    prompt = f"Write a {word_count} blog post about: {topic}"
    
    try:
        response = ollama.generate(model=model, prompt=prompt)
        return response['response']
    except Exception as e:
        return f"Error: {str(e)}"

def generate_email(purpose, recipient_type, tone="professional", model="llama3"):
    """Generate an email."""
    prompt = f"Write a {tone} email to {recipient_type} for the purpose of: {purpose}"
    
    try:
        response = ollama.generate(model=model, prompt=prompt)
        return response['response']
    except Exception as e:
        return f"Error: {str(e)}"

def generate_story(genre, elements, model="llama3"):
    """Generate a short story."""
    prompt = f"Write a {genre} short story that includes: {', '.join(elements)}"
    
    try:
        response = ollama.generate(model=model, prompt=prompt)
        return response['response']
    except Exception as e:
        return f"Error: {str(e)}"

def generate_product_description(product_name, features, model="llama3"):
    """Generate product description."""
    prompt = f"""Write a compelling product description for: {product_name}

Key features:
{chr(10).join(f'- {feature}' for feature in features)}"""
    
    try:
        response = ollama.generate(model=model, prompt=prompt)
        return response['response']
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    try:
        print(generate_blog_post("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
