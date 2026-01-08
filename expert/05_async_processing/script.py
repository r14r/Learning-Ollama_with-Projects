#!/usr/bin/env python3
"""Async Processing Script - Concurrent processing with Ollama."""
import ollama
import asyncio

async def async_generate(prompt, model="llama3"):
    """Asynchronously generate response."""
    try:
        # Note: ollama library may not have native async, so we use run_in_executor
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            lambda: ollama.generate(model=model, prompt=prompt)
        )
        return response['response']
    except Exception as e:
        return f"Error: {str(e)}"

async def process_batch(prompts, model="llama3"):
    """Process multiple prompts concurrently."""
    tasks = [async_generate(prompt, model) for prompt in prompts]
    results = await asyncio.gather(*tasks)
    return results

def main():
    print("=== Async Processing Demo ===\n")
    
    prompts = [
        "Count from 1 to 3",
        "Name 3 colors",
        "List 3 fruits"
    ]
    
    import time
    
    # Sequential processing
    print("Sequential Processing:")
    start = time.time()
    for prompt in prompts:
        response = ollama.generate(model="llama3", prompt=prompt)
        print(f"Prompt: {prompt}")
        print(f"Response: {response['response'][:50]}...\n")
    seq_time = time.time() - start
    print(f"Time: {seq_time:.2f}s\n")
    
    # Async processing
    print("Async Processing:")
    start = time.time()
    results = asyncio.run(process_batch(prompts))
    for prompt, result in zip(prompts, results):
        print(f"Prompt: {prompt}")
        print(f"Response: {result[:50]}...\n")
    async_time = time.time() - start
    print(f"Time: {async_time:.2f}s")
    print(f"Speedup: {seq_time/async_time:.2f}x")

if __name__ == "__main__":
    main()
