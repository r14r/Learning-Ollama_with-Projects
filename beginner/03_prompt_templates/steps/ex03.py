#!/usr/bin/env python3
"""
Prompt Templates Script
Demonstrates how to use prompt templates with Ollama LLM.
"""

import ollama

def create_template(template_str):
    """
    Create a simple template function.
    
    Args:
        template_str (str): Template string with {variable} placeholders
    
    Returns:
        function: Function that fills the template
    """
    def fill_template(**kwargs):
        return template_str.format(**kwargs)
    return fill_template

def use_template(template_func, model="llama3", **kwargs):
    """
    Use a template to generate a prompt and query the LLM.
    
    Args:
        template_func (function): Template function
        model (str): Name of the Ollama model to use
        **kwargs: Variables to fill in the template
    
    Returns:
        str: The LLM's response
    """
    prompt = template_func(**kwargs)
    try:
        response = ollama.chat(
            model=model,
            messages=[
                {
                    'role': 'user',
                    'content': prompt
                }
            ]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    try:
        print(create_template("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
