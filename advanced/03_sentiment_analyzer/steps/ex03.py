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

def main():
    try:
        print(analyze_sentiment("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
