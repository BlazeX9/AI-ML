Machines performs tasks that typically require human intelligence, such as learning, reasoning, problem-solving and decision-making. The goal of **Artificial Intelligence (AI)** is to create systems that can understand information, learn from data and make decisions or perform tasks autonomously.

## Types of AI Based on Capabilities

1. **Narrow AI**: designed to perform a specific task or a limited set of tasks. It cannot operate outside its defined domain. Examples: Siri, Google Search
2. **General AI**: an AI system that can perform any intellectual task a human can, with the ability to reason, learn and apply knowledge across different domains.
3. **Super AI**: a hypothetical form of AI that surpasses human intelligence in all aspects, including reasoning, creativity, problem-solving and emotional intelligence.  

## Generative AI

Generative AI is a type of artificial intelligence designed to create new content such as text, images, music or even code by learning patterns from existing data. These models use techniques like **deep learning** and **neural networks** to generate output. Generative AI is trained on large datasets like text, images, audio or video using deep learning networks.

Text: uses large language models (**LLM**) to predict the next sequence  
Images: uses models like **DALL·E** or **Stable Diffusion** to create realistic visuals  
Video: multimodal systems like Sora by OpenAI, temporally coherent video clips from text or other prompts  

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

## Agentic AI

Agentic AI is a system that can autonomously make decisions, plan actions and execute tasks to achieve specific goals with minimal human intervention. It focuses on goal-driven behavior, reasoning and interaction with tools and environments.

1. Unlike traditional AI systems that primarily respond to inputs, Agentic AI focuses on autonomous decision-making and goal-driven actions  
2. Chatbots uses no tools and gives static response where Agentic AI uses tools and performs dynamic workflows
3. It can connect with and use specific APIs and databases to achieve its goal

## Model Context Protocol (MCP)

MCP is a standardized framework by Anthropic that enables AI models to connect with external tools and data sources, providing secure, scalable and real time access without custom integrations

## Retrieval Augmented Generation (RAG)

RAG is a way to make AI answers more reliable by combining searching for relevant information from external sources (like documents or databases) and then uses it to give a better answer.

1. Use user-specific data to give more relevant responses  
2. No need to retrain the model every time new data comes in  
3. Overcomes LLM restrictions like Hallucinations, Outdated knowledge and access to private documents

External Knowledge Source -> Text Chunking -> Embedding -> Vector Database -> Query Encoder -> Retriever -> LLM -> Response  

Text Chunking: breaks large text into smaller manageable chunks
Embedding: converts text into numerical vectors
Vector Database: stores embeddings and enables similarity search for fast information retrieval
Query Encoder: transforms the user’s query into a vector for comparison with stored embeddings
Retriever: finds and returns the most relevant chunks from the database based on query similarity <br>
![Project Logo](https://media.geeksforgeeks.org/wp-content/uploads/20250210190608027719/How-Rag-works.webp)
