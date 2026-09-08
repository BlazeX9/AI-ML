from dotenv import load_dotenv
import os
load_dotenv()

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"),model="gpt-4.1-mini")

from pypdf import PdfReader
reader = PdfReader("./Information.pdf")
pdf_text = ""

for i in reader.pages:
    text = i.extract_text()
    if text:
        pdf_text += text + "\n"

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
prompt = f"""
You are a PDF reader assistant.
Answer the user's question using ONLY the information available in the PDF.
If the answer is not available in the PDF, say: "I could not find this information in the PDF"

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

    response = llm.invoke(chat_history)
    answer = response.content
    chat_history.append(AIMessage(content=answer))
    print("\nAnswer:", answer)