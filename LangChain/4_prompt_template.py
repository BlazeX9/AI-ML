from dotenv import load_dotenv
import os
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(api_key=os.getenv("GOOGLE_API_KEY"),model="gemini-3.5-flash-lite")

import streamlit as st
st.title("Code Generator")
language_input = st.selectbox(
    "Select Language",
    ["Java", "Python"]
)
topic_input = st.selectbox(
    "Select Topic",
    ["Method Overloading", "Method Overriding", "Inheritance", "Constructor"]
)
style_input = st.selectbox(
    "Select Explanation",
    ["With Example", "Without Example"]
)

from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate(
    template="""
    Generate code as per the selected language type: {language_input}
    on the following selected topic: {topic_input}
    as per the selected style: {style_input}
    Explain in simple english
    """,
    input_variables=[
        "language_input",
        "topic_input",
        "style_input"
    ],
    validate_template=True
)

from langchain_core.output_parsers import StrOutputParser
chain = prompt | llm | StrOutputParser()

if st.button('Generate'):
    result = chain.invoke({
        "language_input": language_input,
        "topic_input": topic_input,
        "style_input": style_input
    })
    st.write(result)