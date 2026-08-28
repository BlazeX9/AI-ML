from dotenv import load_dotenv  
import os  
load_dotenv()  

from langchain_core.tools import tool  
from langchain_google_genai import ChatGoogleGenerativeAI  
llm = ChatGoogleGenerativeAI(api_key=os.getenv("GOOGLE_API_KEY"),model="gemini-3.5-flash-lite")  

### Tool Creation  
@tool  
def multiply_nums(a:int,b:int)->int:  
    """Multiply two numbers"""  
    return a*b  

@tool  
def sum_nums(a:int,b:int)->int:  
    """Sum of thwo numbers"""  
    return a+b  

