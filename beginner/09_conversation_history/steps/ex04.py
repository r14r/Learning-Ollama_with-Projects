#!/usr/bin/env python3
"""
Conversation History Script
Demonstrates how to maintain conversation context/history with Ollama.
"""

import ollama

class ConversationManager:
    """Manages conversation history with an LLM."""
    
    def __init__(self, model="llama3", system_prompt=None):
        """
        Initialize conversation manager.
        
        Args:
            model (str): Name of the Ollama model to use
            system_prompt (str): Optional system prompt
        """
        self.model = model
        self.messages = []
        
        if system_prompt:
            self.messages.append({
                'role': 'system',
                'content': system_prompt
            })
    
    def send_message(self, user_message):
        """
        Send a message and get a response.
        
        Args:
            user_message (str): User's message
        
        Returns:
            str: Assistant's response
        """
        # Add user message to history
        self.messages.append({
            'role': 'user',
            'content': user_message
        })
        
        try:
            # Get response with full history
            response = ollama.chat(
                model=self.model,
                messages=self.messages
            )
            
            assistant_message = response['message']['content']
            
            # Add assistant response to history
            self.messages.append({
                'role': 'assistant',
                'content': assistant_message
            })
            
            return assistant_message
            
        except Exception as e:
            return f"Error: {str(e)}"
    
    def get_history(self):
        """
        Get conversation history.
        
        Returns:
            list: List of messages
        """
        return self.messages.copy()
    
    def clear_history(self):
        """Clear conversation history (keep system prompt if exists)."""
        system_messages = [m for m in self.messages if m['role'] == 'system']
        self.messages = system_messages

def demo_conversation():
    """Demonstrate a multi-turn conversation."""
    print("=== Conversation History Demo ===\n")
    
    # Create conversation manager
    conv = ConversationManager(
        system_prompt="You are a helpful math tutor."
    )
    
    # Turn 1
    print("User: What is 5 + 3?")
    response = conv.send_message("What is 5 + 3?")
    print(f"Assistant: {response}\n")
    
    # Turn 2 - references previous context
    print("User: Now multiply that by 2")
    response = conv.send_message("Now multiply that by 2")
    print(f"Assistant: {response}\n")
    
    # Turn 3 - further context
    print("User: And subtract 4 from the result")
    response = conv.send_message("And subtract 4 from the result")
    print(f"Assistant: {response}\n")
    
    # Show history
    print("=" * 80)
    print("Conversation History:")
    print("=" * 80)
    for i, msg in enumerate(conv.get_history(), 1):
        print(f"{i}. Role: {msg['role']}")
        print(f"   Content: {msg['content'][:100]}...")
        print()

def demo_context_importance():
    """Demonstrate the importance of context."""
    print("\n=== Context Importance Demo ===\n")
    
    # Without context
    print("Without Context:")
    print("-" * 80)
    response = ollama.chat(
        model="llama3",
        messages=[
            {'role': 'user', 'content': 'What is its capital?'}
        ]
    )
    print(f"User: What is its capital?")
    print(f"Assistant: {response['message']['content']}\n")
    
    # With context
    print("With Context:")
    print("-" * 80)
    response = ollama.chat(
        model="llama3",
        messages=[
            {'role': 'user', 'content': 'Tell me about France.'},
            {'role': 'assistant', 'content': 'France is a country in Western Europe.'},
            {'role': 'user', 'content': 'What is its capital?'}
        ]
    )
    print(f"User: What is its capital?")
    print(f"Assistant: {response['message']['content']}")

def main():
    """Main function to demonstrate conversation history."""
    demo_conversation()
    demo_context_importance()

def main():
    try:
        print(demo_conversation())
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
