from ExternalKnowledgeSource import document
from dotenv import load_dotenv
import os
load_dotenv()

#Step 1: Chunking
from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 150,
    chunk_overlap = 25
)

chunks = splitter.create_documents(document)
print("Chunks:",len(chunks))

#Step 2: Embedding Generation
from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"),model="text-embedding-3-small")

#from langchain_google_genai import GoogleGenerativeAIEmbeddings
#embeddings = GoogleGenerativeAIEmbeddings(google_api_key=os.getenv("GOOGLE_API_KEY"),model="models/gemini-embedding-001")

#Step 3: Store to Vector Database
import warnings
warnings.filterwarnings("ignore",message="`langchain-community` is being sunset")

from langchain_community.vectorstores import FAISS
vectors = FAISS.from_documents(chunks,embeddings)
vectors.save_local("./vector_db")
print(vectors.index_to_docstore_id)