from dotenv import load_dotenv
import os
load_dotenv()

from langchain_openai import ChatOpenAI
#from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"),model="gpt-4.1-mini",temperature=0)
#llm = ChatGoogleGenerativeAI(api_key=os.getenv("GOOGLE_API_KEY"),model="gemini-3.5-flash-lite")

from pypdf import PdfReader
reader = PdfReader("./Information.pdf")
pdf_text = ""

for i in reader.pages:
    text = i.extract_text()
    if text:
        pdf_text += text + "\n"

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
chain = llm | StrOutputParser()

prompt = f"""
You are a PDF reader assistant.
Answer the user's question using only the information available in the PDF.
If the answer is not available in the PDF say: "I could not find this information in the PDF"

PDF Content: {pdf_text}
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
