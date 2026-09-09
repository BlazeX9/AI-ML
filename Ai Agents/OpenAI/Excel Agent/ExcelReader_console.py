from dotenv import load_dotenv
import os
load_dotenv()

from openai import OpenAI
llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

import pandas as pd
reader = pd.read_excel("./Information.xlsx")
excel_data = reader.to_string(index=False)  #index=False → Don't include row numbers

prompt = f"""
You are a Excel reader assistant.
Answer the user's question using ONLY the information available in the Excel.
If the answer is not available in the Excel, say: "I could not find this information in the Excel"

Excel Content: {excel_data}
"""

chat_history = [{"role": "system", "content": prompt}]

while True:
    user_input = input("User: ")

    if user_input.strip() == "":
        print("Please ask a question")
        continue

    if user_input.lower() == "exit":
        break

    chat_history.append({"role": "user","content": user_input})

    response = llm.responses.create(
        model="gpt-4.1-mini",
        input=chat_history
    )

    answer = response.output_text
    print("\nAnswer:", answer)
    chat_history.append({"role": "assistant","content": answer})
