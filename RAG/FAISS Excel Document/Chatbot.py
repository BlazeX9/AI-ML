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

    #Prompt Construction
    from langchain_core.prompts import PromptTemplate
    prompt = PromptTemplate(
        template = """
        You are a helpful AI assistant that answers questions based on the provided Excel content.
        Instructions: 
        - Answer the user's question using the information provided in the Excel. 
        - Give accurate, clear and concise answers. 
        - Do not make up or assume information that is not present in the context. 
        - If the answer cannot be found in the Excel say: "I couldn't find the answer in the provided Excel" 
        - If the user's question is not related to the Excel reply that you can only answer questions related to the provided Excel
        
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