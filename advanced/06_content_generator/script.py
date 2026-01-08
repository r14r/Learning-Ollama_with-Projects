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
    """Main function to demonstrate content generation."""
    print("=== Content Generator Demo ===\n")
    
    # Test 1: Blog post
    print("Test 1: Generate Blog Post")
    print("=" * 80)
    post = generate_blog_post("The Future of AI", "short")
    print(f"Topic: The Future of AI")
    print(f"Content:\n{post[:500]}...\n")
    
    # Test 2: Email
    print("\nTest 2: Generate Email")
    print("=" * 80)
    email = generate_email("requesting a meeting", "a colleague", "professional")
    print(f"Purpose: Requesting a meeting")
    print(f"Email:\n{email}\n")
    
    # Test 3: Story
    print("\nTest 3: Generate Story")
    print("=" * 80)
    story = generate_story("science fiction", ["robot", "mystery", "space station"])
    print(f"Genre: Science Fiction")
    print(f"Story:\n{story[:400]}...\n")
    
    # Test 4: Product description
    print("\nTest 4: Product Description")
    print("=" * 80)
    description = generate_product_description(
        "SmartWatch Pro",
        ["Heart rate monitoring", "GPS tracking", "7-day battery", "Waterproof"]
    )
    print(f"Product: SmartWatch Pro")
    print(f"Description:\n{description}")


if __name__ == "__main__":
    main()
