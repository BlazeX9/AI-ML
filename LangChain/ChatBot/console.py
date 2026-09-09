from dotenv import load_dotenv
import os
load_dotenv()

#from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
#llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"),model="gpt-4.1-mini",temperature=0)
llm = ChatGoogleGenerativeAI(api_key=os.getenv("GOOGLE_API_KEY"),model="gemini-3.5-flash-lite")

from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_core.output_parsers import StrOutputParser
chain = llm | StrOutputParser()

prompt = f"""
You are a helpful assistant who replies in simple english and on topic.
You are developed in the year 2026.
You are developed by Abhik Chatterjee.
"""

chat_history = [SystemMessage(content=prompt)]

while True:
    user_input = input("User: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    if user_input.strip() == "":
        print("Please ask a question")
        continue
    
    chat_history.append(HumanMessage(content=user_input))

    ai_response = chain.invoke(chat_history)
    print("Agent:",ai_response)
    chat_history.append(AIMessage(content=ai_response))
