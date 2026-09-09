from dotenv import load_dotenv
import os
load_dotenv()

file_name = input("Enter file name (PDF or Excel): ").strip()
ext = os.path.splitext(file_name)[1].lower()

if not os.path.exists(file_name):
    raise FileNotFoundError(f"File not found: {file_name}")

if ext == ".pdf":
    from pypdf import PdfReader
    reader = PdfReader(file_name)
    raw_text = ""
    for i in reader.pages:
        text = i.extract_text()
        if text:
            raw_text += text + "\n"

elif ext in (".xlsx", ".xls"):
    import pandas as pd
    reader = pd.read_excel(file_name)
    raw_text = reader.to_string(index=False)

else:
    raise ValueError(f"Unsupported file type: {ext}")

from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 25
)

chunks = splitter.create_documents([raw_text])
print("Chunks:", len(chunks))

from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"), model="text-embedding-3-small")

import warnings
warnings.filterwarnings("ignore", message="`langchain-community` is being sunset")

from langchain_community.vectorstores import FAISS
vectors = FAISS.from_documents(chunks, embeddings)
vectors.save_local("./vector_db")