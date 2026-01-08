# Learning Ollama with Projects

A comprehensive collection of 30 Python scripts using Ollama and its Python SDK, organized by difficulty level. Learn to build AI-powered applications with local LLMs through practical, hands-on projects. Each script comes with detailed requirements documentation (Pflichtenheft) describing functionality, inputs, outputs, and tests.

## 📚 Project Structure

This repository contains 30 Ollama projects divided into three difficulty levels:

- **Beginner** (10 projects): Fundamental Ollama concepts and basic LLM interactions
- **Advanced** (10 projects): Real-world applications and advanced features
- **Expert** (10 projects): Complex AI patterns and architectures

Each project is contained in its own directory with:
- `script.py` - The Python implementation using Ollama SDK
- `Pflichtenheft.md` - Requirements document with functionality, I/O specs, and test cases

## 🎯 Beginner Level

Perfect for those starting their Ollama journey. Learn basic LLM interactions and foundational concepts.

| # | Project | Description |
|---|---------|-------------|
| 01 | [Hello LLM](beginner/01_hello_llm) | Basic LLM interaction and model communication |
| 02 | [Simple Chat](beginner/02_simple_chat) | Simple chat interface with a model |
| 03 | [Prompt Templates](beginner/03_prompt_templates) | Working with prompt templates |
| 04 | [Model Info](beginner/04_model_info) | Getting model information and details |
| 05 | [Text Completion](beginner/05_text_completion) | Text completion tasks |
| 06 | [Streaming Response](beginner/06_streaming_response) | Streaming responses for real-time output |
| 07 | [Temperature Control](beginner/07_temperature_control) | Parameter control and model behavior |
| 08 | [System Prompts](beginner/08_system_prompts) | Using system prompts for model behavior |
| 09 | [Conversation History](beginner/09_conversation_history) | Maintaining conversation context |
| 10 | [List Models](beginner/10_list_models) | Listing and managing available models |

## 🚀 Advanced Level

Build real-world AI applications with advanced Ollama features.

| # | Project | Description |
|---|---------|-------------|
| 01 | [Code Assistant](advanced/01_code_assistant) | Code generation and programming assistance |
| 02 | [Summarization Tool](advanced/02_summarization_tool) | Text summarization with LLMs |
| 03 | [Sentiment Analyzer](advanced/03_sentiment_analyzer) | Sentiment analysis of text |
| 04 | [Translation Service](advanced/04_translation_service) | Multi-language translation |
| 05 | [QA System](advanced/05_qa_system) | Question-answering system |
| 06 | [Content Generator](advanced/06_content_generator) | Content generation tool |
| 07 | [Data Extractor](advanced/07_data_extractor) | Extract structured data from text |
| 08 | [Chat with Context](advanced/08_chat_with_context) | Context-aware chatbot |
| 09 | [Few-Shot Learning](advanced/09_few_shot_learning) | Few-shot learning examples |
| 10 | [JSON Mode](advanced/10_json_mode) | Structured JSON responses |

## 💎 Expert Level

Master advanced AI patterns and build sophisticated applications.

| # | Project | Description |
|---|---------|-------------|
| 01 | [RAG System](expert/01_rag_system) | Retrieval Augmented Generation |
| 02 | [Function Calling](expert/02_function_calling) | Function/tool calling patterns |
| 03 | [Multi-Model Ensemble](expert/03_multi_model_ensemble) | Using multiple models together |
| 04 | [Embedding Search](expert/04_embedding_search) | Semantic search with embeddings |
| 05 | [Async Processing](expert/05_async_processing) | Asynchronous/concurrent processing |
| 06 | [Custom Model Adapter](expert/06_custom_model_adapter) | Custom model configuration |
| 07 | [Conversation Manager](expert/07_conversation_manager) | Advanced conversation management |
| 08 | [Prompt Optimizer](expert/08_prompt_optimizer) | Prompt optimization framework |
| 09 | [Model Evaluator](expert/09_model_evaluator) | Model performance evaluation |
| 10 | [AI Agent Framework](expert/10_ai_agent_framework) | Autonomous AI agent system |

## 🛠️ Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Ollama installed and running ([Installation Guide](https://ollama.ai/download))
- At least one model pulled (e.g., `ollama pull llama3`)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/r14r/Learning_Ollama_with-Projects.git
cd Learning_Ollama_with-Projects
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Ensure Ollama is running and pull a model:
```bash
# Check if Ollama is running
ollama list

# Pull a model if needed (e.g., llama3)
ollama pull llama3
```

### Running a Script

Navigate to any project directory and run the script:
```bash
cd beginner/01_hello_llm
python script.py
```

Each script is self-contained and can be run independently.

## 📖 Learning Path

### Recommended Order:

1. **Start with Beginner**: Complete all 10 beginner projects to understand Ollama basics
2. **Move to Advanced**: Build practical AI applications
3. **Challenge with Expert**: Master advanced patterns and architectures

### How to Use Each Project:

1. **Read the Pflichtenheft.md** - Understand the requirements and what the script should do
2. **Study the script.py** - Analyze the implementation and code patterns
3. **Run the script** - See it in action and observe the output
4. **Modify it** - Experiment with changes and parameters
5. **Try the tests** - Verify functionality works as expected

## 🎓 What You'll Learn

### Beginner Level
- Basic Ollama SDK usage
- Model interaction and communication
- Prompt engineering fundamentals
- Response handling and streaming
- Parameter tuning (temperature, top_p, etc.)
- System prompts and conversation history
- Model management

### Advanced Level
- Code generation and assistance
- Text analysis and transformation
- Natural language processing tasks
- Context management
- Few-shot learning techniques
- Structured output generation
- Building practical AI tools

### Expert Level
- Retrieval Augmented Generation (RAG)
- Function calling and tool use
- Multi-model architectures
- Semantic search with embeddings
- Asynchronous processing
- Custom model configurations
- AI agent patterns
- Prompt optimization
- Model evaluation and benchmarking

## 📝 Documentation Format

Each `Pflichtenheft.md` includes:
- **Expected Functionality**: What the script does
- **Input**: What data/parameters it accepts
- **Expected Output**: What results it produces
- **Tests**: Sample test cases with expected results
- **Dependencies**: Required Python packages
- **Usage**: How to run the script

## 🔧 Common Ollama Models

Popular models to use with these projects:
- `llama3` - Meta's Llama 3 model (recommended for beginners)
- `mistral` - Mistral AI's efficient model
- `codellama` - Specialized for code tasks
- `phi3` - Microsoft's compact model
- `gemma2` - Google's Gemma model

Pull a model: `ollama pull <model-name>`

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new projects
- Improve existing code
- Add more test cases
- Enhance documentation

## 📄 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- Built with [Ollama](https://ollama.ai/) and the Ollama Python SDK
- Inspired by practical, hands-on learning approaches
- Created as a comprehensive learning resource for AI developers at all levels

---

**Happy Learning with Ollama! 🤖**