from dotenv import load_dotenv
import os
load_dotenv()

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"),model="gpt-4.1-mini")


#Prompt is the actual instruction given to the LLM
prompt = "Explain about Recursion in python"
response = llm.invoke(prompt)
print(response.content)


#Prompt Template is a reusable structure for creating prompts with variables
from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate(
    template="Explain {topic} in simple English",
    input_variables=["topic"]
)
chain = prompt | llm
response = chain.invoke({"topic": "LangChain"})
print(response.content)
