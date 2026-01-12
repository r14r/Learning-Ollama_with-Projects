#!/usr/bin/env python3
"""Chat with Context Script - Context-aware chatbot using Ollama."""
import ollama

class ContextualChatbot:
    """Chatbot that maintains context across conversations."""
    
    def __init__(self, model="llama3", context_doc=""):
        self.model = model
        self.context_doc = context_doc
        self.messages = []
        if context_doc:
            self.messages.append({'role': 'system', 'content': f"Use this context: {context_doc}"})
    
    def chat(self, user_message):
        """Send message and get response."""
        self.messages.append({'role': 'user', 'content': user_message})
        try:
            response = ollama.chat(model=self.model, messages=self.messages)
            assistant_msg = response['message']['content']
            self.messages.append({'role': 'assistant', 'content': assistant_msg})
            return assistant_msg
        except Exception as e:
            return f"Error: {str(e)}"

def main():
    print("=== Context-Aware Chatbot Demo ===\n")
    
    context = "You are a helpful assistant for a tech company called TechCorp that sells laptops and phones."
    bot = ContextualChatbot(context_doc=context)
    
    print("Bot: Hello! How can I help you?")
    
    questions = [
        "What products do you sell?",
        "Tell me about the laptops.",
        "What about warranty?"
    ]
    
    for q in questions:
        print(f"\nUser: {q}")
        response = bot.chat(q)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
