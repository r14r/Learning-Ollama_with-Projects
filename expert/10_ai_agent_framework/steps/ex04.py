#!/usr/bin/env python3
"""AI Agent Framework - Autonomous agent system."""

import ollama

class AIAgent:
    """Autonomous AI agent with tools."""
    
    def __init__(self, name, tools, model="llama3"):
        self.name = name
        self.tools = tools
        self.model = model
        self.memory = []
    
    def think(self, situation):
        """Agent reasoning."""
        prompt = f"""You are {self.name}. 

Available tools: {', '.join(self.tools.keys())}

Situation: {situation}

What should you do? Choose a tool and explain."""
        
        try:
            response = ollama.generate(model=self.model, prompt=prompt)
            return response['response']
        except Exception as e:
            return f"Error: {str(e)}"
    
    def act(self, action, **params):
        """Execute action."""
        if action in self.tools:
            result = self.tools[action](**params)
            self.memory.append({'action': action, 'result': result})
            return result
        return "Unknown action"

def search_web(query):
    """Simulate web search."""
    return f"Search results for: {query}"

def send_email(to, subject):
    """Simulate sending email."""
    return f"Email sent to {to} with subject: {subject}"

def main():
    print("=== AI Agent Framework Demo ===\n")
    
    tools = {
        'search_web': search_web,
        'send_email': send_email
    }
    
    agent = AIAgent("Assistant Agent", tools)
    
    situation = "User wants to know about Python programming"
    
    print(f"Situation: {situation}\n")
    thinking = agent.think(situation)
    print(f"Agent thinking: {thinking}\n")
    
    result = agent.act('search_web', query="Python programming")
    print(f"Action result: {result}")

def main():
    try:
        print(search_web("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
