Machines performs tasks that typically require human intelligence, such as learning, reasoning, problem-solving and decision-making. The goal of **Artificial Intelligence (AI)** is to create systems that can understand information, learn from data and make decisions or perform tasks autonomously.

## Types of AI Based on Capabilities

1. `Narrow AI`: designed to perform a specific task or a limited set of tasks. It cannot operate outside its defined domain. Examples: Siri, Google Search
2. `General AI`: an AI system that can perform any intellectual task a human can, with the ability to reason, learn and apply knowledge across different domains.
3. `Super AI`: a hypothetical form of AI that surpasses human intelligence in all aspects, including reasoning, creativity, problem-solving and emotional intelligence.  

## Generative AI

Generative AI is a type of artificial intelligence designed to create new content such as text, images, music or even code by learning patterns from existing data. These models use techniques like **deep learning** and **neural networks** to generate output. Generative AI is trained on large datasets like text, images, audio or video using deep learning networks.

Text: uses large language models (**LLM**) to predict the next sequence  
Images: uses models like **DALL·E** or **Stable Diffusion** to create realistic visuals  
Video: multimodal systems like Sora by OpenAI, temporally coherent video clips from text or other prompts  

## Large Language Model (LLM)

LLM is built on **deep neural networks** designed to process, understand and generate human-like text. LLMs store knowledge in the form of parameters. The more parametric knowledge an LLM has the better it can perform. LLMs need to be pre-trained so their knowledge may become outdated depending on when they were last trained. Training an LLM with the latest or private data requires additional training which can be costly and fine-tuning requires deep technical knowledge. Every time the data changes fine-tuning may be needed so this is not a viable option when data needs to be updated very frequently. Some of the modern LLMs are OpenAI ChatGPT, Google Gemini, Anthropic Claude and Meta Llama. 

User input -> Tokenization -> Transformer Model -> Response

With **context learning** a LLM can perform a task or answer questions based on similar type of information already provided, without need of retraining the models parameters.

## Tokenization

Tokenization is the process of breaking **text into smaller pieces called tokens** so that an LLM can process it. A token can be a word, part of a word, punctuation mark or sometimes a character. LLMs process input as tokens not raw text. API usage and pricing are often based on the number of tokens. Tokenization affects how efficiently a model processes text. The same sentence can produce different numbers of tokens depending on the tokenizer.

## Transformer Model

A Transformer is the architecture designed to process and understand sequences of data, especially text. It focuses on understanding relationships within data to process information more effectively. It is the core architecture behind the modern LLMs.

## Agentic AI

Agentic AI is a system that can autonomously make decisions, plan actions and execute tasks to achieve specific goals with minimal human intervention. It focuses on goal-driven behavior, reasoning and interaction with tools and environments.

1. Unlike traditional AI systems that primarily respond to inputs, Agentic AI focuses on autonomous decision-making and goal-driven actions  
2. Chatbots uses no tools and gives static response where Agentic AI uses tools and performs dynamic workflows
3. It can connect with and use specific APIs and databases to achieve its goal

## LangChain

LangChain is an **open-source framework** for developing applications powered by large language models. One benefit of using LangChain is its reusable components, which allow you to easily swap out language models, data sources and processing steps without rewriting the core code.

## Retrieval Augmented Generation (RAG)

RAG is a way to make AI answers more reliable by combining searching for relevant information from external sources (like documents or databases) and then uses it to give a better answer. RAG is **cheaper and easier alternative to retraining/fine-tuning** an LLM when need to provide it with new or private information.  

External Knowledge Source -> Text Chunking -> Embedding -> Vector Database -> Query Encoder -> Retriever -> Augmentation -> Response  

`Text Chunking`: Breaks large documents into small, semantically meaningful chunks  
`Embedding`: Converts each chunk into numerical vectors  
`Vector Database`: Stores embeddings and enables similarity search for fast information retrieval  
`Query Encoder`: Transforms the user's query into a vector for comparison with stored embeddings  
`Retriever`: Finds and returns the most relevant chunks from the database based on query similarity   
`Augmentation`: At this step, retrieved documents are combined with the user's query to form a new enriched prompt for the LLM<br>

`Hallucination`: Traditional generative models can produce incorrect or fabricated information. RAG reduces this risk by retrieving relevant and verified external data as context.  
`FAISS**: Facebook AI Similarity Search is a library developed by Meta for storing and efficiently searching vector embeddings. It performs fast similarity searches to find vectors that are most similar to a given query.  
`Semantic Search`: 

## Model Context Protocol (MCP)

MCP is a standardized framework by Anthropic that enables AI models to connect with external tools and data sources, providing secure, scalable and real time access without custom integrations

## Ollama

Ollama is a platform that allows users to run LLMs locally on their own machines. This allows users to interact with AI models without relying entirely on cloud-based APIs. Some of the LLMs are Llama, Gemma, Qwen, DeepSeek, Mistral

Install Ollama on machine -> Open terminal or command prompt -> Download and run a model -> ollama run llama3.2

see the models installed on your machine: ollama list  
download a model: ollama pull llama3.2
