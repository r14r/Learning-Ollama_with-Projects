#!/usr/bin/env python3
"""
List Models Script
Demonstrates how to list, manage, and work with available Ollama models.
"""

import ollama
from datetime import datetime

def list_all_models():
    """
    List all available Ollama models.
    
    Returns:
        list: List of model dictionaries
    """
    try:
        result = ollama.list()
        return result.get('models', [])
    except Exception as e:
        print(f"Error listing models: {e}")
        return []

def format_bytes(bytes_size):
    """
    Format bytes to human-readable size.
    
    Args:
        bytes_size (int): Size in bytes
    
    Returns:
        str: Formatted size string
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.2f} PB"

def display_models_table(models):
    """
    Display models in a formatted table.
    
    Args:
        models (list): List of model dictionaries
    """
    if not models:
        print("No models found.")
        print("\nTo pull a model, run:")
        print("  ollama pull llama3")
        return
    
    print(f"\n{'Name':<30} {'Size':<15} {'Modified':<20}")
    print("=" * 65)
    
    for model in models:
        name = model.get('name', 'Unknown')
        size = format_bytes(model.get('size', 0))
        modified = model.get('modified_at', '')
        
        # Format date if available
        if modified:
            try:
                dt = datetime.fromisoformat(modified.replace('Z', '+00:00'))
                modified = dt.strftime('%Y-%m-%d %H:%M')
            except:
                pass
        
        print(f"{name:<30} {size:<15} {modified:<20}")

def main():
    try:
        print(list_all_models())
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
