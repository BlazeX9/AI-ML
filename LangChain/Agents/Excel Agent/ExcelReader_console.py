from dotenv import load_dotenv
import os
load_dotenv()

from langchain_openai import ChatOpenAI
#from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"),model="gpt-4.1-mini",temperature=0)
#llm = ChatGoogleGenerativeAI(api_key=os.getenv("GOOGLE_API_KEY"),model="gemini-3.5-flash-lite")

import pandas as pd
reader = pd.read_excel("./Information.xlsx")
excel_data = reader.to_string(index=False)

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
chain = llm | StrOutputParser()

prompt = f"""
You are a Excel reader assistant.
Answer the user's question using only the information available in the Excel.
If the answer is not available in the Excel say: "I could not find this information in the Excel"

Excel Content: {excel_data}
"""

chat_history = [SystemMessage(content=prompt)]

while True:
    user_input = input("User: ")

    if user_input.strip() == "":
        print("Please ask a question")
        continue

    if user_input.lower() == "exit":
        break

    chat_history.append(HumanMessage(content=user_input))

    ai_response = chain.invoke(chat_history)
    print("Answer:",ai_response)
    chat_history.append(AIMessage(content=ai_response))