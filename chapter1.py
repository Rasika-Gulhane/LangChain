# Integrating code with OpenAI API




# Integrating code with OpenAI API


import os
from constants import openai_key
from langchain.llms import OpenAI
import streamlit as st
from langchain import PromptTemplate
from langchain.chains import LLMChain

from langchain.chains import SequentialChain
from langchain.memory import ConversationBufferMemory
os.environ['OPENAI_API_KEY']= openai_key


#Streamlit framework like FLASK

st.title("Celebrity Search result")
input_text = st.text_input("Search the topic u want")




# prompt template

first_prompt = PromptTemplate(
    input_variables = ['name'],
    template= "Tell me something about Celebrity {name}"
)



person_memory = ConversationBufferMemory(input_key='name', memory_key='chat_history')
dob_memory = ConversationBufferMemory(input_key='person', memory_key='chat_history')
description_memory = ConversationBufferMemory(input_key='dob', memory_key='description_history')


# OpenAI LLMs
llm = OpenAI(temperature= 0.8)
chain = LLMChain(llm= llm, prompt= first_prompt, verbose=True, output_key = 'person', memory=person_memory)  


# prompt template

second_prompt = PromptTemplate(
    input_variables = ['person'],
    template= "When was the {person} born"
)


chain2 = LLMChain(llm= llm, prompt= second_prompt, verbose=True, output_key = 'dob', memory=dob_memory)   


third_prompt = PromptTemplate(
    input_variables = ['dob'],
    template= "Mentioned 4 major event happen around {dob} in the world"
)


chain3 = LLMChain(llm= llm, prompt= third_prompt, verbose=True, output_key = 'description', memory=description_memory)  



parent_chain = SequentialChain(
    chains =[chain,chain2, chain3], input_variables =['name'], 
    output_variables =['person','dob', 'description'], verbose=True)



if input_text:
    st.write(parent_chain({'name': input_text}))

    with st.expander('Person Name'):
        st.info(person_memory.buffer)

    with st.expander('Major event'):
        st.info(description_memory.buffer)




