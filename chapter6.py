# Modules

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser     #default output parser

import streamlit as st
import os


# Fetch Environmnet variable from constants import
from constants import openai_key, langchain_api_key

os.environ['OPENAI_API_KEY']= openai_key

#for deploymnet and LangSmith Tracking

os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['LANGCHAIN_API_KEY']= langchain_api_key

# streamlit Framework

st.title("LANGCHAIN Based LLM SEARCH with Open AI")
input_text = st.text_input("Search the topic u want")


# Prompt for LLM

prompt = ChatPromptTemplate.from_messages(
    [
        ( "system", "Act as an assiatant. Please response to user queries"),
        ( "user", "Question: {question}")
    ]
)


# Model building with OpenAI
llm = ChatOpenAI(model= "gpt-3.5-turbo")
outputparser= StrOutputParser()
chain = prompt|llm|outputparser


# Output for asked input 

if input_text:
    st.write(chain.invoke({"question": input_text}))    
