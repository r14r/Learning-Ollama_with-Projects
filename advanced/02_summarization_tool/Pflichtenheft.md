# Pflichtenheft: Summarization Tool

## Expected Functionality
This script provides text summarization capabilities using Ollama LLM. It can create summaries of various lengths, bullet-point summaries, extract key points, and generate audience-specific summaries.

## Input
- **Function parameters**:
  - `text` (str): Text to summarize
  - `length` (str, optional): "short", "medium", or "long"
  - `num_points` (int, optional): Number of bullet points
  - `audience` (str, optional): Target audience description
  - `model` (str, optional, default: "llama3"): Model to use

## Expected Output
```
=== Text Summarization Demo ===

Test 1: Short Summary
================================================================================
Original Text: [long text about AI]

Short Summary:
AI has transformed industries through machine learning and deep learning, but ethical concerns remain.

Test 2: Bullet Point Summary
================================================================================
Summary (3 points):
• AI and machine learning are transforming multiple industries
• Deep learning achieves remarkable results in various applications
• Ethical concerns about bias and job displacement persist

Test 3: Extract Key Points
================================================================================
Key Points:
1. AI transforms industries through data processing
2. Deep learning uses neural networks
3. Companies invest heavily in AI
4. Ethical concerns exist
```

## Tests

### Test 1: Short Summary
**Input:** `summarize_text(long_text, "short")`  
**Expected Output:** 1-2 sentence summary

### Test 2: Medium Summary
**Input:** `summarize_text(long_text, "medium")`  
**Expected Output:** 3-5 sentence summary

### Test 3: Bullet Points
**Input:** `summarize_bullets(text, 5)`  
**Expected Output:** 5 bullet points

### Test 4: Key Points Extraction
**Input:** `extract_key_points(text)`  
**Expected Output:** List of main ideas

### Test 5: Audience-Specific
**Input:** `summarize_for_audience(text, "experts")`  
**Expected Output:** Technical summary for experts

### Test 6: Children Audience
**Input:** `summarize_for_audience(text, "children")`  
**Expected Output:** Simple, easy-to-understand summary

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
- Implement text summarization with LLMs
- Control summary length and format
- Extract key information
- Adapt content for different audiences
- Apply prompt engineering for summarization
- Build practical NLP tools
