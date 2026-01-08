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


def format_size(bytes_size):
    """
    Format byte size to human-readable format.
    
    Args:
        bytes_size (int): Size in bytes
    
    Returns:
        str: Formatted size
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.2f} PB"


def main():
    """Main function to demonstrate model information retrieval."""
    print("=== Ollama Model Information ===\n")
    
    # List all models
    print("Available Models:")
    print("-" * 80)
    models = list_models()
    
    if not models:
        print("No models found. Please pull a model first:")
        print("  ollama pull llama3")
        return
    
    for model in models:
        name = model.get('name', 'Unknown')
        size = model.get('size', 0)
        modified = model.get('modified_at', '')
        
        print(f"Name: {name}")
        print(f"Size: {format_size(size)}")
        if modified:
            print(f"Modified: {modified}")
        print("-" * 80)
    
    # Show detailed info for the first model
    if models:
        first_model = models[0]['name']
        print(f"\nDetailed Information for '{first_model}':")
        print("=" * 80)
        
        info = show_model_info(first_model)
        
        if info:
            # Display key information
            if 'modelfile' in info:
                print("\nModelfile:")
                print(info['modelfile'][:500] + "..." if len(info['modelfile']) > 500 else info['modelfile'])
            
            if 'parameters' in info:
                print("\nParameters:")
                print(info['parameters'][:300] + "..." if len(info['parameters']) > 300 else info['parameters'])
            
            if 'template' in info:
                print("\nTemplate:")
                print(info['template'][:200] + "..." if len(info['template']) > 200 else info['template'])


if __name__ == "__main__":
    main()
