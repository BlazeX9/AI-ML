from dotenv import load_dotenv
import os
load_dotenv()

from pypdf import PdfReader
reader = PdfReader("./Information.pdf")
pdf_text = ""

for i in reader.pages:
    text = i.extract_text()
    if text:
        pdf_text += text + "\n"

from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 25
)

chunks = splitter.create_documents([pdf_text])
print("Chunks:",len(chunks))

from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"),model="text-embedding-3-small")

#from langchain_google_genai import GoogleGenerativeAIEmbeddings
#embeddings = GoogleGenerativeAIEmbeddings(google_api_key=os.getenv("GOOGLE_API_KEY"),model="models/gemini-embedding-001")

import warnings
warnings.filterwarnings("ignore",message="`langchain-community` is being sunset")

from langchain_community.vectorstores import FAISS
vectors = FAISS.from_documents(chunks,embeddings)
vectors.save_local("./vector_db")
#print(vectors.index_to_docstore_id)