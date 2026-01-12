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
    """Main function to demonstrate prompt templates."""
    print("=== Prompt Templates Demo ===\n")
    
    # Template 1: Translation
    print("Template 1: Translation")
    translation_template = create_template(
        "Translate the following text to {language}: '{text}'"
    )
    result = use_template(
        translation_template,
        language="Spanish",
        text="Hello, how are you?"
    )
    print(f"Result: {result}\n")
    
    # Template 2: Summarization
    print("Template 2: Summarization")
    summary_template = create_template(
        "Summarize the following text in {num_sentences} sentences: {text}"
    )
    result = use_template(
        summary_template,
        num_sentences="2",
        text="Python is a high-level programming language. It was created by Guido van Rossum and released in 1991. Python emphasizes code readability and allows programmers to express concepts in fewer lines of code."
    )
    print(f"Result: {result}\n")
    
    # Template 3: Question with context
    print("Template 3: Question with Context")
    qa_template = create_template(
        "Context: {context}\n\nQuestion: {question}"
    )
    result = use_template(
        qa_template,
        context="The Eiffel Tower is a wrought-iron lattice tower in Paris, France. It was built in 1889.",
        question="When was the Eiffel Tower built?"
    )
    print(f"Result: {result}")

def main():
    try:
        print(create_template("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
