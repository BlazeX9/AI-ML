from dotenv import load_dotenv
import os
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(api_key=os.getenv("GOOGLE_API_KEY"),model="gemini-3.1-flash-lite")

from langchain_google_genai import GoogleGenerativeAIEmbeddings
#from langchain_openai import OpenAIEmbeddings
embeddings = GoogleGenerativeAIEmbeddings(google_api_key=os.getenv("GOOGLE_API_KEY"),model="models/gemini-embedding-001")
#embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"),model="text-embedding-3-small")

from langchain_community.vectorstores import FAISS
vectors = FAISS.load_local("./vector_db",embeddings,allow_dangerous_deserialization=True)

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break
    
    retriever = vectors.as_retriever(search_type="similarity",search_kwags={"k": 4})
    restriver_res = retriever.invoke(user_input)

    context_text = ""
    for i in restriver_res: 
        context_text = context_text + i.page_content

    #Augmentation
    from langchain_core.prompts import PromptTemplate
    prompt = PromptTemplate(
        template = """
        You are a helpful assistant. 
        Use the following pieces of context to answer the question. 
        If you don't know the answer, just say that you don't know, don't try to make up an answer.

        {context}
        Question: {question}
        """,
        input_variables = ['context','question']
    )

    final_prompt = prompt.invoke({"context": context_text,"question": user_input})

    #Generation
    from langchain_core.output_parsers import StrOutputParser
    chain = llm | StrOutputParser()

    answer = chain.invoke(final_prompt)
    print(answer)