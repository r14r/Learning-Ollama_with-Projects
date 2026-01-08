#!/usr/bin/env python3
"""Custom Model Adapter - Create custom model configurations."""
import ollama

class ModelAdapter:
    """Adapter for custom model configurations."""
    
    def __init__(self, base_model="llama3"):
        self.base_model = base_model
        self.default_options = {}
    
    def set_persona(self, persona):
        """Set model persona."""
        self.system_prompt = f"You are {persona}."
    
    def configure(self, **options):
        """Configure model options."""
        self.default_options.update(options)
    
    def generate(self, prompt):
        """Generate with custom configuration."""
        messages = []
        if hasattr(self, 'system_prompt'):
            messages.append({'role': 'system', 'content': self.system_prompt})
        messages.append({'role': 'user', 'content': prompt})
        
        try:
            response = ollama.chat(
                model=self.base_model,
                messages=messages,
                options=self.default_options
            )
            return response['message']['content']
        except Exception as e:
            return f"Error: {str(e)}"

def main():
    print("=== Custom Model Adapter Demo ===\n")
    
    # Create specialized adapter
    expert = ModelAdapter()
    expert.set_persona("an expert programmer")
    expert.configure(temperature=0.3)
    
    creative = ModelAdapter()
    creative.set_persona("a creative storyteller")
    creative.configure(temperature=1.2)
    
    prompt = "Write about a robot."
    
    print("Expert (low temperature):")
    print(expert.generate(prompt)[:200] + "...\n")
    
    print("Creative (high temperature):")
    print(creative.generate(prompt)[:200] + "...")

if __name__ == "__main__":
    main()
