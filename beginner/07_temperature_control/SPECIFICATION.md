# Pflichtenheft: Temperature Control

## Expected Functionality
This script demonstrates how to control LLM output using temperature and other parameters. Temperature affects randomness and creativity: low values (0.0-0.3) produce focused, deterministic outputs, while high values (1.0+) produce more creative and varied outputs.

## Input
- **Function parameters**:
  - `prompt` (str): User prompt
  - `temperature` (float): Temperature value (0.0 to 2.0)
  - `model` (str, optional, default: "llama3"): Name of the Ollama model to use
  - `**options`: Additional parameters (top_p, top_k, etc.)

## Expected Output
```
=== Temperature Control Demo ===

Test 1: Low Temperature (0.0) - More Focused and Deterministic
================================================================================
Prompt: What is 2+2?
Response: The answer is 4.

Test 2: High Temperature (1.5) - More Creative and Random
================================================================================
Prompt: Write a creative name for a space cat.
Response: Nebula Whiskers McPounce, the Cosmic Feline Explorer!

Test 3: Temperature Comparison
================================================================================
Prompt: Complete this: The ocean is

Temperature: 0.0
--------------------------------------------------------------------------------
vast and deep.

Temperature: 0.5
--------------------------------------------------------------------------------
a magnificent body of water covering most of Earth's surface.

Temperature: 1.0
--------------------------------------------------------------------------------
an incredible ecosystem teeming with diverse marine life.

Temperature: 1.5
--------------------------------------------------------------------------------
a mysterious realm where ancient creatures dance beneath moonlit waves.
```

## Tests

### Test 1: Low Temperature
**Input:** `generate_with_temperature("What is 2+2?", 0.0)`  
**Expected Output:** Consistent, deterministic answer "4"

### Test 2: High Temperature
**Input:** `generate_with_temperature("Write a creative name", 1.5)`  
**Expected Output:** Creative, varied response

### Test 3: Temperature Comparison
**Input:** `compare_temperatures("The sky is")`  
**Expected Output:** 4 different responses showing increasing creativity

### Test 4: Multiple Options
**Input:** `generate_with_options("Test", temperature=0.5, top_p=0.9)`  
**Expected Output:** Response influenced by multiple parameters

### Test 5: Edge Cases
**Input:** `generate_with_temperature("Test", 0.0)` run twice  
**Expected Output:** Nearly identical responses

## Dependencies
```
ollama>=0.1.0
```

## Prerequisites
- Ollama must be installed and running
- At least one model must be pulled (e.g., `ollama pull llama3`)

## Usage
```bash
python script.py
```

## Learning Objectives
- Understand temperature parameter and its effects
- Use the options parameter in Ollama
- Compare model behavior at different settings
- Apply appropriate temperatures for different tasks
- Understand top_p, top_k, and other parameters
