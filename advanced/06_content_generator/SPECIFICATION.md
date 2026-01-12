# Pflichtenheft: Content Generator

## Expected Functionality
This script generates various types of content including blog posts, emails, stories, and product descriptions using Ollama LLM.

## Input
- **Function parameters**:
  - `topic` (str): Topic for blog post
  - `purpose` (str): Email purpose
  - `genre` (str): Story genre
  - `product_name` (str): Product name
  - `features` (list): Product features
  - `length` (str, optional): Content length
  - `tone` (str, optional): Writing tone
  - `model` (str, optional, default: "llama3"): Model to use

## Expected Output
```
=== Content Generator Demo ===

Test 1: Generate Blog Post
Topic: The Future of AI
Content:
Artificial Intelligence is transforming our world...

Test 2: Generate Email
Purpose: Requesting a meeting
Email:
Subject: Meeting Request
Dear Colleague,...

Test 3: Generate Story
Genre: Science Fiction
Story:
On the space station, Detective...
```

## Tests
### Test 1: Blog Post
**Input:** `generate_blog_post("AI", "short")`  
**Expected Output:** ~300 word blog post

### Test 2: Email
**Input:** `generate_email("thank you", "client")`  
**Expected Output:** Professional thank you email

### Test 3: Story
**Input:** `generate_story("mystery", ["detective", "clue"])`  
**Expected Output:** Short mystery story

## Dependencies
```
ollama>=0.1.0
```

## Usage
```bash
python script.py
```

## Learning Objectives
- Generate different content types
- Control tone and style
- Apply content generation patterns
