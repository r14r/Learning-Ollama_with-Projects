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


def verify_answer(question, answer, context, model="llama3"):
    """
    Verify if an answer is correct given context.
    
    Args:
        question (str): Original question
        answer (str): Proposed answer
        context (str): Context information
        model (str): Model to use
    
    Returns:
        str: Verification result
    """
    prompt = f"""Context: {context}

Question: {question}
Proposed Answer: {answer}

Is this answer correct based on the context? Explain."""
    
    try:
        response = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    """Main function to demonstrate QA system."""
    print("=== Question-Answering System Demo ===\n")
    
    # Sample context
    context = """
    Python was created by Guido van Rossum and first released in 1991. 
    It is an interpreted, high-level programming language with dynamic typing. 
    Python emphasizes code readability and uses significant indentation.
    The Python Software Foundation manages the development of Python.
    """
    
    # Test 1: Answer with context
    print("Test 1: Answer with Context")
    print("=" * 80)
    question = "When was Python first released?"
    answer = answer_question(question, context)
    print(f"Context: {context.strip()}\n")
    print(f"Question: {question}")
    print(f"Answer: {answer}\n")
    
    # Test 2: Multiple questions from document
    print("Test 2: Multiple Questions from Document")
    print("=" * 80)
    questions = [
        "Who created Python?",
        "What type of language is Python?",
        "Which organization manages Python development?"
    ]
    for q in questions:
        ans = answer_from_document(q, context)
        print(f"Q: {q}")
        print(f"A: {ans}\n")
    
    # Test 3: Verify answer
    print("Test 3: Verify Answer")
    print("=" * 80)
    question = "When was Python created?"
    proposed_answer = "1991"
    verification = verify_answer(question, proposed_answer, context)
    print(f"Question: {question}")
    print(f"Proposed Answer: {proposed_answer}")
    print(f"Verification: {verification}")


if __name__ == "__main__":
    main()
