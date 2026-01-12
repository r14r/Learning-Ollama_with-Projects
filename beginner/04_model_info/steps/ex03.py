#!/usr/bin/env python3
"""
Model Info Script
Demonstrates how to get information about Ollama models.
"""

import ollama
from datetime import datetime

def list_models():
    """
    List all available models.
    
    Returns:
        list: List of model information dictionaries
    """
    try:
        models = ollama.list()
        return models.get('models', [])
    except Exception as e:
        print(f"Error listing models: {e}")
        return []

def show_model_info(model_name):
    """
    Show detailed information about a specific model.
    
    Args:
        model_name (str): Name of the model
    
    Returns:
        dict: Model information
    """
    try:
        info = ollama.show(model_name)
        return info
    except Exception as e:
        print(f"Error getting model info: {e}")
        return {}

def main():
    try:
        print(list_models())
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
