Machines performs tasks that typically require human intelligence, such as learning, reasoning, problem-solving and decision-making. The goal of **Artificial Intelligence (AI)** is to create systems that can understand information, learn from data and make decisions or perform tasks autonomously.

## Types of AI Based on Capabilities

1. **Narrow AI**: Designed to perform a specific task or a limited set of tasks. It cannot operate outside its defined domain. Examples: Siri, Google Search
2. **General AI**: An AI system that can perform any intellectual task a human can, with the ability to reason, learn and apply knowledge across different domains.
3. **Super AI**: A hypothetical form of AI that surpasses human intelligence in all aspects, including reasoning, creativity, problem-solving and emotional intelligence.  

## Generative AI

Generative AI is a type of artificial intelligence designed to create new content such as text, images, music or even code by learning patterns from existing data. These models use techniques like **deep learning** and **neural networks** to generate output. Generative AI is trained on large datasets like text, images, audio or video using deep learning networks.

Text: Uses large language models (**LLM**) to predict the next sequence  
Images: Uses models like **DALL·E** or **Stable Diffusion** to create realistic visuals  
Video: Multimodal systems like Sora by OpenAI, temporally coherent video clips from text or other prompts  

## Large Language Model (LLM)

LLM is advanced AI systems built on **deep neural networks** designed to process, understand and generate human-like text. Some of the modern LLMs are OpenAI ChatGPT, Google Gemini, Anthropic Claude and Meta Llama

1. LLM can generate creative prompts and answer questions  
2. LLM can generate code, assist in identifying code errors and suggest fixes  
3. LLM can translate across many languages  

User input -> Tokenization -> Transformer Model -> Response

## Tokenization

Tokenization is the process of breaking text into smaller pieces called tokens so that an LLM can process it. A token can be a word, part of a word, punctuation mark or sometimes a character. LLMs process input as tokens not raw text. API usage and pricing are often based on the number of tokens. Tokenization affects how efficiently a model processes text. The same sentence can produce different numbers of tokens depending on the tokenizer.

## Transformer Model

A Transformer is the architecture designed to process and understand sequences of data, especially text. It focuses on understanding relationships within data to process information more effectively. It is the core architecture behind the modern LLMs.

## Ollama

Ollama is a platform that allows users to run LLMs locally on their own machines. This allows users to interact with AI models without relying entirely on cloud-based APIs. Some of the LLMs are Llama, Gemma, Qwen, DeepSeek, Mistral

Install Ollama on machine -> Open terminal or command prompt -> Download and run a model -> ollama run llama3.2

see the models installed on your machine: ollama list  
download a model: ollama pull llama3.2
