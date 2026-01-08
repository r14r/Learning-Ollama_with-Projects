#!/usr/bin/env python3
"""Function Calling Script - Implement function/tool calling with Ollama."""
import ollama
import json

def get_weather(location):
    """Simulate weather API."""
    return f"Weather in {location}: Sunny, 22°C"

def calculate(operation, a, b):
    """Perform calculation."""
    ops = {'+': a+b, '-': a-b, '*': a*b, '/': a/b if b != 0 else "Error"}
    return ops.get(operation, "Unknown operation")

TOOLS = {
    "get_weather": get_weather,
    "calculate": calculate
}

def function_calling_agent(user_request, model="llama3"):
    """Agent that can call functions."""
    prompt = f"""User request: {user_request}

Available functions:
- get_weather(location): Get weather for a location
- calculate(operation, a, b): Perform math operation

Respond with JSON if function call needed:
{{"function": "function_name", "args": {{"arg1": "value1"}}}}

Or respond directly if no function needed."""
    
    try:
        response = ollama.generate(model=model, prompt=prompt)
        result = response['response'].strip()
        
        # Try to parse as function call
        try:
            if '{' in result and '}' in result:
                func_call = json.loads(result)
                func_name = func_call.get('function')
                args = func_call.get('args', {})
                
                if func_name in TOOLS:
                    output = TOOLS[func_name](**args)
                    return f"Function: {func_name}\nResult: {output}"
        except:
            pass
        
        return result
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("=== Function Calling Demo ===\n")
    
    requests = [
        "What's the weather in Paris?",
        "Calculate 15 + 27",
        "Tell me a joke"
    ]
    
    for req in requests:
        print(f"Request: {req}")
        result = function_calling_agent(req)
        print(f"Response: {result}\n")

if __name__ == "__main__":
    main()
