#Tool creation
from langchain_core.tools import tool

@tool
def multiply(a:int,b:int)->int:
    """Multiply two numbers"""
    return a*b

print(multiply.name)
print(multiply.description)
print(multiply.args)


#Bulit-in DuckDuckGo Search
from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()
result = search_tool.invoke("Latest news in india today on Business!")
print(result)