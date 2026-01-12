#!/usr/bin/env python3
"""Few-Shot Learning Script - Teach tasks with examples using Ollama."""
import ollama

def few_shot_classify(text, examples, model="llama3"):
    """Classify using few-shot examples."""
    prompt = "Learn from these examples:\n\n"
    for ex in examples:
        prompt += f"Input: {ex['input']}\nOutput: {ex['output']}\n\n"
    prompt += f"Now classify this:\nInput: {text}\nOutput:"
    
    try:
        response = ollama.generate(model=model, prompt=prompt)
        return response['response']
    except Exception as e:
        return f"Error: {str(e)}"

def few_shot_generate(task, examples, input_text, model="llama3"):
    """Generate using few-shot examples."""
    prompt = f"Task: {task}\n\nExamples:\n"
    for ex in examples:
        prompt += f"Input: {ex['input']}\nOutput: {ex['output']}\n\n"
    prompt += f"Your turn:\nInput: {input_text}\nOutput:"
    
    try:
        response = ollama.generate(model=model, prompt=prompt)
        return response['response']
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("=== Few-Shot Learning Demo ===\n")
    
    # Sentiment classification examples
    examples = [
        {"input": "I love this!", "output": "Positive"},
        {"input": "This is terrible.", "output": "Negative"},
        {"input": "It's okay.", "output": "Neutral"}
    ]
    
    print("Test 1: Few-Shot Classification")
    result = few_shot_classify("This is amazing!", examples)
    print(f"Input: This is amazing!")
    print(f"Classification: {result}\n")
    
    # Translation examples
    trans_examples = [
        {"input": "Hello", "output": "Hola"},
        {"input": "Goodbye", "output": "Adiós"}
    ]
    
    print("Test 2: Few-Shot Translation")
    result = few_shot_generate("Translate to Spanish", trans_examples, "Thank you")
    print(f"Input: Thank you")
    print(f"Translation: {result}")

if __name__ == "__main__":
    main()
