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

def find_model(model_name):
    """
    Find a specific model by name.
    
    Args:
        model_name (str): Name or partial name of model
    
    Returns:
        dict or None: Model info if found
    """
    models = list_all_models()
    
    for model in models:
        if model_name.lower() in model.get('name', '').lower():
            return model
    
    return None

def get_model_families(models):
    """
    Group models by family (base model name).
    
    Args:
        models (list): List of model dictionaries
    
    Returns:
        dict: Models grouped by family
    """
    families = {}
    
    for model in models:
        name = model.get('name', '')
        # Extract base name (before : or first tag)
        base_name = name.split(':')[0]
        
        if base_name not in families:
            families[base_name] = []
        families[base_name].append(model)
    
    return families

def main():
    """Main function to demonstrate model listing and management."""
    print("=== Ollama Model Manager ===\n")
    
    # Test 1: List all models
    print("Test 1: List All Models")
    print("=" * 80)
    models = list_all_models()
    display_models_table(models)
    
    if not models:
        print("\n⚠️  No models found. Please pull at least one model:")
        print("   ollama pull llama3")
        return
    
    # Test 2: Show count
    print(f"\n\nTest 2: Model Statistics")
    print("=" * 80)
    print(f"Total models: {len(models)}")
    
    total_size = sum(m.get('size', 0) for m in models)
    print(f"Total size: {format_bytes(total_size)}")
    
    # Test 3: Group by family
    print(f"\n\nTest 3: Models by Family")
    print("=" * 80)
    families = get_model_families(models)
    
    for family, family_models in families.items():
        print(f"\n{family} ({len(family_models)} variant(s)):")
        for model in family_models:
            print(f"  - {model.get('name')}")
    
    # Test 4: Find specific model
    print(f"\n\nTest 4: Find Specific Model")
    print("=" * 80)
    
    if models:
        # Search for the first model
        first_model_name = models[0]['name'].split(':')[0]
        found = find_model(first_model_name)
        
        if found:
            print(f"Found: {found.get('name')}")
            print(f"Size: {format_bytes(found.get('size', 0))}")
        else:
            print("Model not found")
    
    # Test 5: Recommendations
    print(f"\n\nTest 5: Popular Models for Different Tasks")
    print("=" * 80)
    recommendations = {
        "General use": ["llama3", "mistral", "phi3"],
        "Code": ["codellama", "deepseek-coder"],
        "Small/Fast": ["phi3", "gemma2:2b"],
        "Large/Powerful": ["llama3:70b", "mixtral"]
    }
    
    for category, model_list in recommendations.items():
        print(f"\n{category}:")
        for model in model_list:
            installed = "✓" if find_model(model) else "✗"
            print(f"  {installed} {model}")

def main():
    try:
        print(list_all_models())
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
