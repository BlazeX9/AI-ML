**`chunk_size:`** maximum size of each chunk  

If a document has 250 characters, its divided roughly like:  
Chunk 1 → characters 1–100  
Chunk 2 → characters 81–180  
Chunk 3 → characters 161–250  

**`chunk_overlap:`** how much content is repeated between consecutive chunks  
Chunk 1: "Python is a programming language that is very popular"  
Chunk 2: "very popular for data science and AI"  
The repeated characters helps while doing RAG/vector search.  
