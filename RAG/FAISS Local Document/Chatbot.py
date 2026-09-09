from dotenv import load_dotenv
import os
load_dotenv()

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"),model="gpt-4.1-mini",temperature=0)

from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"),model="text-embedding-3-small")

#from langchain_google_genai import ChatGoogleGenerativeAI
#llm = ChatGoogleGenerativeAI(api_key=os.getenv("GOOGLE_API_KEY"),model="gemini-3.5-flash-lite")

#from langchain_google_genai import GoogleGenerativeAIEmbeddings
#embeddings = GoogleGenerativeAIEmbeddings(google_api_key=os.getenv("GOOGLE_API_KEY"),model="models/gemini-embedding-002")

import warnings
warnings.filterwarnings("ignore",message="`langchain-community` is being sunset")
from langchain_community.vectorstores import FAISS
vectors = FAISS.load_local("./vector_db",embeddings,allow_dangerous_deserialization=True)

while True:
    user_input = input("User: ")

    if user_input.strip() == "":
        print("Ask your question!")
        continue

    if user_input.lower() == "exit":
        break

    #Retrieval
    retriever = vectors.as_retriever(search_type="similarity",search_kwargs={"k": 4})
    restriver_res = retriever.invoke(user_input)

    context_text = ""
    for i in restriver_res: 
        context_text = context_text + i.page_content

    #Reranking

    #Prompt Construction
    from langchain_core.prompts import PromptTemplate
    prompt = PromptTemplate(
        template = """
        You are a helpful AI assistant that answers questions based on the provided document context.
        Instructions: 
        - Answer the user's question using the information provided in the context. 
        - Give accurate, clear, and concise answers. 
        - Do not make up or assume information that is not present in the context. 
        - If the answer cannot be found in the context say: "I couldn't find the answer in the provided document" 
        - If the user's question is not related to the document, politely mention that you can only answer questions related to the provided document
        
        Context: {context}
        User Question: {question}
        Answer: 
        """,
        input_variables = ['context','question']
    )

    final_prompt = prompt.invoke({"context": context_text,"question": user_input})

    #LLM Answer Generation
    from langchain_core.output_parsers import StrOutputParser
    chain = llm | StrOutputParser()

    answer = chain.invoke(final_prompt)
    print(answer)