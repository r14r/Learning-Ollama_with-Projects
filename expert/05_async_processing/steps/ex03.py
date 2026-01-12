#!/usr/bin/env python3
"""Async Processing Script - Concurrent processing with Ollama."""

import ollama
import asyncio

async def async_generate(prompt, model="llama3"):
    """Asynchronously generate response."""
    try:
        # Use run_in_executor for compatibility with ollama library
        loop = asyncio.get_running_loop()
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
    try:
        print(async_generate("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
