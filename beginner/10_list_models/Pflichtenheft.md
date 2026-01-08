# Pflichtenheft: List Models

## Expected Functionality
This script demonstrates how to list, manage, and work with available Ollama models. It shows model information, grouping, search capabilities, and provides recommendations for different use cases.

## Input
- **Function parameters**:
  - `model_name` (str): Name or partial name to search for
  - `models` (list): List of model dictionaries
  - No user input required for basic execution

## Expected Output
```
=== Ollama Model Manager ===

Test 1: List All Models
================================================================================
Name                           Size            Modified            
=================================================================
llama3:latest                  4.66 GB         2024-01-08 10:30    
mistral:latest                 4.11 GB         2024-01-07 15:20    

Test 2: Model Statistics
================================================================================
Total models: 2
Total size: 8.77 GB

Test 3: Models by Family
================================================================================

llama3 (1 variant(s)):
  - llama3:latest

mistral (1 variant(s)):
  - mistral:latest

Test 4: Find Specific Model
================================================================================
Found: llama3:latest
Size: 4.66 GB

Test 5: Popular Models for Different Tasks
================================================================================

General use:
  ✓ llama3
  ✗ mistral
  ✗ phi3
```

## Tests

### Test 1: List Models
**Input:** `list_all_models()`  
**Expected Output:** List of installed models with details

### Test 2: Format Bytes
**Input:** `format_bytes(4664729600)`  
**Expected Output:** "4.34 GB"

### Test 3: Display Table
**Input:** `display_models_table(models)`  
**Expected Output:** Formatted table with columns

### Test 4: Find Model
**Input:** `find_model("llama")`  
**Expected Output:** First model matching "llama" or None

### Test 5: Group by Family
**Input:** `get_model_families(models)`  
**Expected Output:** Dictionary with models grouped by base name

### Test 6: No Models
**Input:** `list_all_models()` with no models installed  
**Expected Output:** Empty list and helpful message

## Dependencies
```
ollama>=0.1.0
```

## Prerequisites
- Ollama must be installed and running
- At least one model should be pulled for meaningful output

## Usage
```bash
# Ensure at least one model is available
ollama pull llama3

# Run the script
python script.py
```

## Learning Objectives
- Use ollama.list() to get available models
- Parse and display model information
- Format data for display
- Search and filter models
- Group and categorize models
- Provide user recommendations
- Handle cases with no models
