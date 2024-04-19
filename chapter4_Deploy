# Integrating code with OpenAI API


from langchain.llms import OpenAI
import streamlit as st
import os
from constants import openai_key


os.environ['OPENAI_API_KEY']= openai_key

def get_openai_response(question):
    llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature = 0.8)

    response = llm(question)
    return response

# initilaize streamlit app to run

st.set_page_config(page_title="Q&A with LLM Demo")

# Rest of your Streamlit app code
# st.title("Welcome to my App ")
st.header("LLM: Langchain Application")
input = st.text_input("Input: ", key = "input")
response= get_openai_response(input)

submit =st.button("Answer my question")

# submit function on click
if submit:
    st.subheader("The Response is:")
    st.write(response)

