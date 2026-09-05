from ExternalKnowledgeSource import document
from dotenv import load_dotenv
import os
load_dotenv()

#Step 1: Text Chunking
from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 150,
    chunk_overlap = 25
)

chunks = splitter.create_documents(document)
print("Chunks:",len(chunks))
#print(chunks[0],chunks[1],chunks[2])

#Step 2: Text Embedding
from langchain_google_genai import GoogleGenerativeAIEmbeddings
#from langchain_openai import OpenAIEmbeddings
embeddings = GoogleGenerativeAIEmbeddings(google_api_key=os.getenv("GOOGLE_API_KEY"),model="models/gemini-embedding-001")
#embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"),model="text-embedding-3-small")

#Step 3: Indexing
from langchain_community.vectorstores import FAISS
vectors = FAISS.from_documents(chunks,embeddings)
print(vectors.index_to_docstore_id)

#Step 4: Store vectors locally
vectors.save_local("./vector_db")
