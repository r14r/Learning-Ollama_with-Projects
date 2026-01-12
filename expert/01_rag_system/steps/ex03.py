#!/usr/bin/env python3
"""RAG System Script - Retrieval Augmented Generation with Ollama."""

import ollama

class SimpleRAG:
    """Simple RAG system using Ollama."""
    
    def __init__(self, documents, model="llama3"):
        self.documents = documents
        self.model = model
    
    def retrieve(self, query, top_k=2):
        """Simple keyword-based retrieval."""
        scored = []
        for doc in self.documents:
            score = sum(1 for word in query.lower().split() if word in doc.lower())
            scored.append((score, doc))
        scored.sort(reverse=True)
        return [doc for _, doc in scored[:top_k]]
    
    def generate(self, query):
        """Generate answer using retrieved context."""
        context_docs = self.retrieve(query)
        context = "\n\n".join(context_docs)
        
        prompt = f"""Use this context to answer the question:

Context:
{context}

Question: {query}

Answer based on the context:"""
        
        try:
            response = ollama.chat(
                model=self.model,
                messages=[{'role': 'user', 'content': prompt}]
            )
            return response['message']['content']
        except Exception as e:
            return f"Error: {str(e)}"

def main():
    print("=== RAG System Demo ===\n")
    
    # Sample knowledge base
    documents = [
        "Python was created by Guido van Rossum and released in 1991.",
        "Python is known for its simple syntax and readability.",
        "JavaScript was created by Brendan Eich in 1995.",
        "JavaScript is primarily used for web development.",
        "Machine learning is a subset of artificial intelligence."
    ]
    
    rag = SimpleRAG(documents)
    
    questions = [
        "Who created Python?",
        "When was JavaScript created?",
        "What is Python known for?"
    ]
    
    for question in questions:
        print(f"Question: {question}")
        answer = rag.generate(question)
        print(f"Answer: {answer}\n")

def main():
    print("Step 3: Kernbausteine geladen.")

if __name__ == "__main__":
    main()
