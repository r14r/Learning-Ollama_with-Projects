#!/usr/bin/env python3
"""Multi-Model Ensemble Script - Use multiple models together."""
import ollama

class ModelEnsemble:
    """Ensemble of multiple models."""
    
    def __init__(self, models):
        self.models = models
    
    def query_all(self, prompt):
        """Query all models and return responses."""
        responses = {}
        for model in self.models:
            try:
                response = ollama.generate(model=model, prompt=prompt)
                responses[model] = response['response']
            except Exception as e:
                responses[model] = f"Error: {str(e)}"
        return responses
    
    def consensus_answer(self, question):
        """Get consensus answer from multiple models."""
        responses = self.query_all(question)
        
        # Synthesize responses
        synthesis_prompt = f"""Question: {question}

Different AI models gave these answers:
"""
        for model, answer in responses.items():
            synthesis_prompt += f"\n{model}: {answer}\n"
        
        synthesis_prompt += "\nProvide a consensus answer:"
        
        try:
            response = ollama.generate(model=self.models[0], prompt=synthesis_prompt)
            return response['response']
        except Exception as e:
            return f"Error: {str(e)}"

def main():
    print("=== Multi-Model Ensemble Demo ===\n")
    
    # Use available models (adjust as needed)
    models = ["llama3"]  # Add more: ["llama3", "mistral", "phi3"]
    ensemble = ModelEnsemble(models)
    
    question = "What is the capital of France?"
    
    print(f"Question: {question}\n")
    print("Individual Responses:")
    responses = ensemble.query_all(question)
    for model, response in responses.items():
        print(f"{model}: {response}\n")
    
    print("\nConsensus Answer:")
    consensus = ensemble.consensus_answer(question)
    print(consensus)

if __name__ == "__main__":
    main()
