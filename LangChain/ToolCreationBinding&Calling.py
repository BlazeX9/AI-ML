from dotenv import load_dotenv
import os
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
#from langchain_openai import ChatOpenAI
llm = ChatGoogleGenerativeAI(api_key=os.getenv("GOOGLE_API_KEY"),model="gemini-3.5-flash-lite")
#llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"),model="gpt-4.1-mini")

#Tool Creation
from langchain_core.tools import tool
@tool
def multiply_nums(a:int,b:int)->int:
    """Multiply two numbers"""
    return a*b

@tool
def sum_nums(a:int,b:int)->int:
    """Sum of two numbers"""
    return a+b

#Tool Binding
llm_tools = llm.bind_tools([multiply_nums,sum_nums])

tools_map = {
    "multiply_nums": multiply_nums,
    "sum_nums": sum_nums
}

#Tool Calling: LLM decides which tool to use
while True:
    user_input = input("User: ")

    if user_input.lower() == "exit":
        break

    user_query_res = llm_tools.invoke(user_input)
    toolname = None

    if user_query_res.tool_calls:
        toolname = user_query_res.tool_calls[0]["name"]
        toolargs = user_query_res.tool_calls[0]["args"]
        print("Tool called! Tool name:", toolname)

        if toolname in tools_map:
            print("Answer:",tools_map[toolname].invoke(toolargs))
    else:
        print("No tool called! Answer:", user_query_res.content[0]["text"])
