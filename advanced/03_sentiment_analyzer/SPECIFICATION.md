# Pflichtenheft: Sentiment Analyzer

## Expected Functionality
This script analyzes the sentiment and emotions in text using Ollama LLM. It can determine if text is positive, negative, or neutral, provide sentiment scores, identify emotions, and process multiple texts in batch.

## Input
- **Function parameters**:
  - `text` (str): Text to analyze
  - `texts` (list): List of texts for batch analysis
  - `model` (str, optional, default: "llama3"): Model to use

## Expected Output
```
=== Sentiment Analyzer Demo ===

Test 1: Basic Sentiment Analysis
================================================================================

Text (positive): I absolutely love this product! It exceeded all my expectations...
Analysis: Positive - The text expresses strong enthusiasm and satisfaction.

Text (negative): This is terrible. Worst experience ever...
Analysis: Negative - Strong negative language and disappointment.

Test 2: Sentiment Scoring
================================================================================
Text: I absolutely love this product!...
Score: +0.9 - Highly positive sentiment with enthusiastic language.

Test 3: Emotion Detection
================================================================================
Text: I'm so excited and happy! This is the best day ever!
Emotions: Joy, Excitement, Happiness
```

## Tests

### Test 1: Positive Sentiment
**Input:** `analyze_sentiment("I love this!")`  
**Expected Output:** "Positive" classification with explanation

### Test 2: Negative Sentiment
**Input:** `analyze_sentiment("This is terrible.")`  
**Expected Output:** "Negative" classification with explanation

### Test 3: Neutral Sentiment
**Input:** `analyze_sentiment("The sky is blue.")`  
**Expected Output:** "Neutral" classification

### Test 4: Sentiment Score
**Input:** `sentiment_score("Amazing product!")`  
**Expected Output:** High positive score (close to +1)

### Test 5: Emotion Detection
**Input:** `analyze_emotion("I'm so angry!")`  
**Expected Output:** "Anger" identified

### Test 6: Batch Processing
**Input:** `batch_sentiment_analysis([text1, text2, text3])`  
**Expected Output:** List of sentiment results for all texts

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
- Implement sentiment analysis with LLMs
- Classify text sentiment (positive/negative/neutral)
- Score sentiment intensity
- Detect emotions in text
- Process multiple texts efficiently
- Apply NLP for text analysis
- Build practical sentiment analysis tools
