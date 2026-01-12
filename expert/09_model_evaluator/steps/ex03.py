#!/usr/bin/env python3
"""Model Evaluator - Evaluate model performance."""

import ollama
import time

class ModelEvaluator:
    """Evaluates model performance."""
    
    def __init__(self, model="llama3"):
        self.model = model
    
    def evaluate_latency(self, prompts):
        """Measure response latency."""
        latencies = []
        for prompt in prompts:
            start = time.time()
            try:
                ollama.generate(model=self.model, prompt=prompt)
                latencies.append(time.time() - start)
            except:
                latencies.append(None)
        
        valid = [l for l in latencies if l is not None]
        return {
            'avg': sum(valid) / len(valid) if valid else 0,
            'min': min(valid) if valid else 0,
            'max': max(valid) if valid else 0
        }
    
    def evaluate_accuracy(self, test_cases):
        """Evaluate accuracy on test cases."""
        correct = 0
        for case in test_cases:
            response = ollama.generate(model=self.model, prompt=case['prompt'])
            answer = response['response'].lower()
            if case['expected'].lower() in answer:
                correct += 1
        return correct / len(test_cases) if test_cases else 0

def main():
    print("=== Model Evaluator Demo ===\n")
    
    evaluator = ModelEvaluator()
    
    # Test latency
    prompts = ["What is 2+2?", "Name a color", "Count to 3"]
    print("Evaluating Latency...")
    latency = evaluator.evaluate_latency(prompts)
    print(f"Average: {latency['avg']:.2f}s")
    print(f"Min: {latency['min']:.2f}s")
    print(f"Max: {latency['max']:.2f}s\n")
    
    # Test accuracy
    test_cases = [
        {'prompt': 'What is 2+2?', 'expected': '4'},
        {'prompt': 'Capital of France?', 'expected': 'Paris'}
    ]
    print("Evaluating Accuracy...")
    accuracy = evaluator.evaluate_accuracy(test_cases)
    print(f"Accuracy: {accuracy*100:.1f}%")

def main():
    print("Step 3: Kernbausteine geladen.")

if __name__ == "__main__":
    main()
