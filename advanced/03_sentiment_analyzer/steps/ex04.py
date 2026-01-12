#!/usr/bin/env python3
"""
Sentiment Analyzer Script
Analyze sentiment of text using Ollama LLM.
"""

import ollama

def analyze_sentiment(text, model="llama3"):
    """
    Analyze the sentiment of text.
    
    Args:
        text (str): Text to analyze
        model (str): Model to use
    
    Returns:
        str: Sentiment analysis result
    """
    prompt = f"""Analyze the sentiment of this text. 
Respond with: Positive, Negative, or Neutral, followed by a brief explanation.

Text: {text}"""
    
    try:
        response = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def sentiment_score(text, model="llama3"):
    """
    Get sentiment score from -1 (negative) to +1 (positive).
    
    Args:
        text (str): Text to analyze
        model (str): Model to use
    
    Returns:
        str: Sentiment score and explanation
    """
    prompt = f"""Rate the sentiment of this text on a scale from -1 (very negative) to +1 (very positive).
Provide the score and explanation.

Text: {text}"""
    
    try:
        response = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def analyze_emotion(text, model="llama3"):
    """
    Identify emotions in text.
    
    Args:
        text (str): Text to analyze
        model (str): Model to use
    
    Returns:
        str: Emotion analysis
    """
    prompt = f"""Identify the main emotions in this text (e.g., joy, anger, sadness, fear, surprise).

Text: {text}"""
    
    try:
        response = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def batch_sentiment_analysis(texts, model="llama3"):
    """
    Analyze sentiment for multiple texts.
    
    Args:
        texts (list): List of texts to analyze
        model (str): Model to use
    
    Returns:
        list: List of sentiment results
    """
    results = []
    for i, text in enumerate(texts, 1):
        print(f"Analyzing text {i}/{len(texts)}...")
        sentiment = analyze_sentiment(text, model)
        results.append({'text': text, 'sentiment': sentiment})
    return results

def main():
    try:
        print(analyze_sentiment("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
