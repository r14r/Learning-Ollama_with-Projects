#!/usr/bin/env python3
"""
QA System Script
Question-answering system using Ollama LLM with context.
"""

import ollama

def answer_question(question, context="", model="llama3"):
    """
    Answer a question, optionally with context.
    
    Args:
        question (str): Question to answer
        context (str): Context information
        model (str): Model to use
    
    Returns:
        str: Answer
    """
    if context:
        prompt = f"Context: {context}\n\nQuestion: {question}\n\nAnswer:"
    else:
        prompt = question
    
    try:
        response = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def answer_from_document(question, document, model="llama3"):
    """
    Answer question based on document content.
    
    Args:
        question (str): Question
        document (str): Document text
        model (str): Model to use
    
    Returns:
        str: Answer extracted from document
    """
    prompt = f"""Based on the following document, answer this question:

Document:
{document}

Question: {question}

Answer based only on the information in the document:"""
    
    try:
        response = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    try:
        print(answer_question("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
