**`chunk_size:`** maximum size of each chunk  

If a document has 250 characters, its divided roughly like:  
Chunk 1 → characters 1–100  
Chunk 2 → characters 81–180  
Chunk 3 → characters 161–250  

**`chunk_overlap:`** how much content is repeated between consecutive chunks  

Chunk 1: "Python is a programming language that is very popular"  
Chunk 2: "very popular for data science and AI"  
The repeated characters helps while doing RAG/vector search.  

**`search_kwargs`** how many most similar chunks retriever gets

## RAG Pipeline

1. Document Ingestion  
   - Accept PDF, DOCX, Excel, CSV, HTML etc  
   - Validate file type, size, permissions and metadata  
   - Store original documents in object storage such as S3/Azure Blob  
  
2. Data Cleaning & Extraction  
   - Remove unnecessary whitespace, headers/footers, duplicate content, corrupted characters etc  
   - Use OCR for images
  
3. Chunking  
   - Split documents into meaningful chunks  
   - Use recursive, semantic or structure-aware chunking depending on the document  
   - Add appropriate chunk overlap  
  
4. Embedding Generation  
   - Convert each chunk into a vector using an embedding model  
   - OpenAI: `text-embedding-3-small`  
  
5. Vector Database  
   - Store embeddings + chunk text + metadata in a vector database  
   - Ex: FAISS, Qdrant, Pinecone, Weaviate, Milvus, pgvector  

6. Query Processing  
   - Clean/normalize the user asked question  

7. Retrieval  
   - Convert the query into an embedding  
   - Perform similarity search  
   - Retrieve Top-K relevant chunks  
  
8. Reranking  
   - Send retrieved candidates to a reranker  
   - Reorder them based on their actual relevance to the question  

9. Prompt Construction  
    - Create a prompt containing System instructions, User question, Retrieved context, Conversation history and Rules  
  
10. LLM Generation  
    - Send the prompt to an LLM to generate the final answer  
   
11. Guardrails & Security  
    - Unauthorized document access  
    - PII/sensitive data  
    - Malicious files  
    - Hallucination prevention  
