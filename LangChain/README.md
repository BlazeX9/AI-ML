```python
from dotenv import load_dotenv

import os

load_dotenv()

from langchain_core.tools import tool

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(api_key=os.getenv("GOOGLE_API_KEY"),model="gemini-3.5-flash-lite")

#from langchain_openai import ChatOpenAI

#llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"),model="gpt-4.1-mini")

#Tool Creation

@tool

def multiply_nums(a:int,b:int)->int:

    """Multiply two numbers"""

    return a*b

@tool

def sum_nums(a:int,b:int)->int:

    """Sum of thwo numbers"""

    return a+b

#Tool Binding

llm_tools = llm.bind_tools([multiply_nums,sum_nums])

tools_map = {

    "multiply_nums": multiply_nums,

    "sum_nums": sum_nums

}

#Tool Calling: LLM only suggest which tool to use the execution is handled by langchain

user_query_res = llm_tools.invoke("Name 10 popular programming languages name only!")

print("Content:", user_query_res.content[0]["text"])

print("Tool suggested by LLM:",user_query_res.tool_calls)

print("Tokens:", user_query_res.usage_metadata["total_tokens"])

user_query_res = llm_tools.invoke("what is multiply of 3 and 4?")

print("Content:", user_query_res.content)

print("Tool suggested by LLM:",user_query_res.tool_calls[0]["name"])

print("Tokens:", user_query_res.usage_metadata["total_tokens"])

#Tool Execution

toolname = user_query_res.tool_calls[0]["name"] #toolname returns string output, tools_map is used to match toolname wtih string value

toolargs = user_query_res.tool_calls[0]["args"]

for i in tools_map:

    if toolname == i:

        print(tools_map[i].invoke(toolargs))

        #print(tools_map[i].invoke(user_query_res.tool_calls[0]))   #Output as ToolMessage
