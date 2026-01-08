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


def translate_multiple_languages(text, languages, model="llama3"):
    """
    Translate text to multiple languages.
    
    Args:
        text (str): Text to translate
        languages (list): List of target languages
        model (str): Model to use
    
    Returns:
        dict: Translations by language
    """
    translations = {}
    for lang in languages:
        print(f"Translating to {lang}...")
        translations[lang] = translate(text, lang, model=model)
    return translations


def translate_with_context(text, target_language, context, model="llama3"):
    """
    Translate with additional context for better accuracy.
    
    Args:
        text (str): Text to translate
        target_language (str): Target language
        context (str): Context information
        model (str): Model to use
    
    Returns:
        str: Translated text
    """
    prompt = f"""Context: {context}

Translate this text to {target_language}, considering the context:

{text}"""
    
    try:
        response = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    """Main function to demonstrate translation."""
    print("=== Translation Service Demo ===\n")
    
    # Test 1: Simple translation
    print("Test 1: English to Spanish")
    print("=" * 80)
    text = "Hello, how are you today?"
    translation = translate(text, "Spanish")
    print(f"Original: {text}")
    print(f"Translation: {translation}\n")
    
    # Test 2: Language detection
    print("Test 2: Language Detection")
    print("=" * 80)
    samples = [
        "Bonjour, comment allez-vous?",
        "Guten Tag, wie geht es Ihnen?",
        "こんにちは、お元気ですか？"
    ]
    for sample in samples:
        detected = detect_language(sample)
        print(f"Text: {sample}")
        print(f"Language: {detected}\n")
    
    # Test 3: Multiple languages
    print("Test 3: Translate to Multiple Languages")
    print("=" * 80)
    text = "Good morning!"
    languages = ["Spanish", "French", "German"]
    translations = translate_multiple_languages(text, languages)
    print(f"Original: {text}\n")
    for lang, trans in translations.items():
        print(f"{lang}: {trans}")
    
    # Test 4: Context-aware translation
    print("\n\nTest 4: Context-Aware Translation")
    print("=" * 80)
    text = "The bank is closed."
    context = "Talking about a financial institution, not a river bank."
    translation = translate_with_context(text, "Spanish", context)
    print(f"Text: {text}")
    print(f"Context: {context}")
    print(f"Translation: {translation}")


if __name__ == "__main__":
    main()
