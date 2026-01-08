# Pflichtenheft: Translation Service

## Expected Functionality
This script provides multi-language translation capabilities using Ollama LLM. It can translate text between languages, detect languages, translate to multiple languages at once, and perform context-aware translation.

## Input
- **Function parameters**:
  - `text` (str): Text to translate
  - `target_language` (str): Target language name
  - `source_language` (str, optional, default: "auto"): Source language
  - `languages` (list): List of target languages
  - `context` (str, optional): Additional context for translation
  - `model` (str, optional, default: "llama3"): Model to use

## Expected Output
```
=== Translation Service Demo ===

Test 1: English to Spanish
================================================================================
Original: Hello, how are you today?
Translation: Hola, ¿cómo estás hoy?

Test 2: Language Detection
================================================================================
Text: Bonjour, comment allez-vous?
Language: French

Text: Guten Tag, wie geht es Ihnen?
Language: German

Test 3: Translate to Multiple Languages
================================================================================
Original: Good morning!

Spanish: ¡Buenos días!
French: Bonjour!
German: Guten Morgen!
```

## Tests

### Test 1: English to Spanish
**Input:** `translate("Hello", "Spanish")`  
**Expected Output:** "Hola"

### Test 2: Detect Language
**Input:** `detect_language("Bonjour")`  
**Expected Output:** "French"

### Test 3: Auto-detect Source
**Input:** `translate("Hola", "English", source_language="auto")`  
**Expected Output:** "Hello"

### Test 4: Multiple Target Languages
**Input:** `translate_multiple_languages("Hi", ["Spanish", "French"])`  
**Expected Output:** Dictionary with translations

### Test 5: Context-Aware Translation
**Input:** `translate_with_context("bank", "Spanish", "financial institution")`  
**Expected Output:** Translation appropriate for financial context

### Test 6: Long Text
**Input:** `translate(long_text, "French")`  
**Expected Output:** Complete French translation

## Dependencies
```
ollama>=0.1.0
```

## Prerequisites
- Ollama must be installed and running
- At least one model must be pulled (e.g., `ollama pull llama3`)
- Models with multilingual capabilities work best

## Usage
```bash
python script.py
```

## Learning Objectives
- Implement translation with LLMs
- Handle multiple languages
- Detect source languages
- Provide context for better translations
- Batch translate to multiple languages
- Build practical translation tools
- Understand multilingual LLM capabilities
