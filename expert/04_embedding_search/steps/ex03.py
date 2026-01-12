#!/usr/bin/env python3
"""Embedding Search Script - Semantic search using Ollama embeddings."""

import ollama

class EmbeddingSearch:
    """Semantic search using embeddings."""
    
    def __init__(self, documents, model="llama3"):
        self.documents = documents
        self.model = model
        self.embeddings = self._embed_documents()
    
    def _embed_documents(self):
        """Generate embeddings for documents."""
        embeddings = []
        for doc in self.documents:
            try:
                emb = ollama.embeddings(model=self.model, prompt=doc)
                embeddings.append(emb['embedding'])
            except Exception as e:
                print(f"Error embedding document: {e}")
                print(f"Note: Embeddings may not be supported by all models.")
                embeddings.append([])
        return embeddings
    
    def search(self, query, top_k=3):
        """Search for similar documents."""
        try:
            query_emb = ollama.embeddings(model=self.model, prompt=query)
            query_vec = query_emb['embedding']
            
            # Cosine similarity
            similarities = []
            for i, doc_emb in enumerate(self.embeddings):
                if doc_emb:
                    similarity = self._cosine_similarity(query_vec, doc_emb)
                    similarities.append((similarity, i))
            
            similarities.sort(reverse=True)
            results = [self.documents[i] for _, i in similarities[:top_k]]
            return results
        except Exception as e:
            return [f"Error: {str(e)}"]
    
    def _cosine_similarity(self, vec1, vec2):
        """Calculate cosine similarity."""
        dot = sum(a*b for a, b in zip(vec1, vec2))
        mag1 = sum(a*a for a in vec1) ** 0.5
        mag2 = sum(b*b for b in vec2) ** 0.5
        return dot / (mag1 * mag2) if mag1 and mag2 else 0

def main():
    print("=== Embedding Search Demo ===\n")
    
    documents = [
        "Python is a programming language",
        "Dogs are loyal pets",
        "JavaScript is used for web development",
        "Cats are independent animals",
        "Machine learning uses Python"
    ]
    
    search = EmbeddingSearch(documents)
    
    queries = [
        "programming languages",
        "pet animals"
    ]
    
    for query in queries:
        print(f"Query: {query}")
        results = search.search(query, top_k=2)
        print("Top results:")
        for i, result in enumerate(results, 1):
            print(f"  {i}. {result}")
        print()

def main():
    print("Step 3: Kernbausteine geladen.")

if __name__ == "__main__":
    main()
