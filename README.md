# Reflection Agent

This repository contains an implementation of the Reflection Pattern, which utilizes a language model (e.g., `llama-3.1-70b-versatile`) for iterative content generation and refinement. By using structured prompts, iterative feedback, and configurable parameters, the Reflection Agent can generate high-quality responses across various applications like code generation, language translation, and summarization.

## Table of Contents

- [Setup Guide](#setup-guide)
- [Usage Examples](#usage-examples)
- [Implementation Guide](#implementation-guide)

---

## Setup Guide

### Prerequisites
- Python 3.7 or higher
- Groq Client API (required to interact with the Groq language model)

### Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:chongchen1999/ReflectionAgent.git
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the Groq API key:
   - Obtain an API key from Groq (or a compatible model provider).
   - Add your API key to your environment:
     ```bash
     GROQ_API_KEY="Your Groq api key here"
     ```

## Usage Examples

### Basic Example

You can quickly test the Reflection Agent by running an example prompt. This example initiates a content generation and reflection cycle with a sample prompt requesting a Python quicksort implementation.

```python
from reflection_agent import ReflectionAgent

# Initialize the agent
agent = ReflectionAgent(model_name="llama-3.1-70b-versatile")

# Run the agent with a prompt
prompt = "Generate a Python implementation of the quicksort algorithm."
result = agent.run(prompt, n_steps=5)

print("Final Output:", result)
```

In this example:
- `n_steps` sets the maximum number of refinement steps.
- The agent generates content based on the initial prompt and refines it based on the model's self-critique until it reaches an optimal result or completes all iterations.

### Testing Reflection in Code Generation

You can test the agent’s performance in code generation by using `examples.py`:
```bash
python examples.py
```
This script tests the agent’s end-to-end functionality, showing each generation and reflection step.

## Implementation Guide

The Reflection Agent is organized into modular files for maintainability and clarity:

- **`reflection_agent.py`**: Contains the main `ReflectionAgent` class, which manages the generation and reflection cycles.
- **`generate.py`** and **`reflect.py`**: Implement functions for generating initial responses and reflecting on them, respectively.
- **`utils.py`**: Provides helper functions and classes for managing chat history, structured prompts, and more.

### Key Components

- **Generation Mechanism**:
  - `ReflectionAgent` initializes with a model and begins the content generation cycle using a structured prompt.
  - After each generation, the content is appended to the chat history.

- **Reflection Quality**:
  - The `reflect_on_response` function assesses each iteration's output, generating critiques that improve response quality.
  - The reflection process stops early if no further improvements are necessary, indicated by an `<OK>` response.

- **Iteration Control**:
  - The `n_steps` parameter limits the maximum number of refinement cycles to optimize computational efficiency.

- **Error Handling**:
  - Chat history is managed to prevent memory overflow, and verbose output provides status updates for easier debugging.

## Video Demo
    - https://www.youtube.com/watch?v=e4sjeOyQ6C0