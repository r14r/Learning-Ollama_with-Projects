#!/usr/bin/env python3
"""Advanced Conversation Manager with features."""
import ollama
import json
from datetime import datetime

class AdvancedConversationManager:
    """Manages conversations with advanced features."""
    
    def __init__(self, model="llama3", max_history=10):
        self.model = model
        self.messages = []
        self.max_history = max_history
        self.metadata = {'created': datetime.now().isoformat()}
    
    def add_message(self, role, content):
        """Add message to history."""
        self.messages.append({
            'role': role,
            'content': content,
            'timestamp': datetime.now().isoformat()
        })
        if len(self.messages) > self.max_history:
            self.messages = self.messages[-self.max_history:]
    
    def chat(self, user_message):
        """Send message and get response."""
        self.add_message('user', user_message)
        
        # Prepare messages for API (remove timestamps)
        api_messages = [{'role': m['role'], 'content': m['content']} for m in self.messages]
        
        try:
            response = ollama.chat(model=self.model, messages=api_messages)
            assistant_msg = response['message']['content']
            self.add_message('assistant', assistant_msg)
            return assistant_msg
        except Exception as e:
            return f"Error: {str(e)}"
    
    def save(self, filename):
        """Save conversation to file."""
        import os
        # Ensure directory exists
        os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
        with open(filename, 'w') as f:
            json.dump({
                'metadata': self.metadata,
                'messages': self.messages
            }, f, indent=2)
    
    def load(self, filename):
        """Load conversation from file."""
        with open(filename, 'r') as f:
            data = json.load(f)
            self.metadata = data['metadata']
            self.messages = data['messages']

def main():
    print("=== Advanced Conversation Manager Demo ===\n")
    
    conv = AdvancedConversationManager(max_history=5)
    
    print("User: Hello!")
    print(f"Bot: {conv.chat('Hello!')}\n")
    
    print("User: Remember this number: 42")
    print(f"Bot: {conv.chat('Remember this number: 42')}\n")
    
    print("User: What number did I tell you?")
    print(f"Bot: {conv.chat('What number did I tell you?')}\n")
    
    # Save conversation to a cross-platform location
    import tempfile
    import os
    save_path = os.path.join(tempfile.gettempdir(), 'conversation.json')
    conv.save(save_path)
    print(f"Conversation saved to {save_path}")

if __name__ == "__main__":
    main()
