
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser     #default output parser
from langchain_community.llms import Ollama
 
import streamlit as st
import os


# Fetch Environmnet variable from constants import
from constants import langchain_api_key

# os.environ['OPENAI_API_KEY']= openai_key # no need since we are using ollama opensouce 

#for deploymnet and LangSmith Tracking 

os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['LANGCHAIN_API_KEY']= langchain_api_key



# Prompt for LLM

prompt = ChatPromptTemplate.from_messages(
    [
        ( "system", "Act as an assiatant. Please response to user queries"),
        ( "user", "Question: {question}")
    ]
)



# streamlit Framework

st.title("Langchain Based LLM SEARCH with Ollama")
input_text = st.text_input("Search the topic u want")


# Ollama LLM

llm = Ollama(model= 'llama2')
outputparser= StrOutputParser()
chain = prompt|llm|outputparser


if input_text:
    st.write(chain.invoke({"question": input_text}))    