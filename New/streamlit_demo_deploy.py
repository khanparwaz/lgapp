import os
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.globals import set_debug

set_debug(True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(model="gpt-4o-mini"
               #, api_key="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"
               )

st.title("Ask Anything")

with st.sidebar:
 st.title("Provide your API Key First")
 openai_key = st.text_input("OpenAI API Key", type="password")

if not openai_key:
 st.info("Enter your OpenAI API Key to continue")
 st.stop()

question = st.text_input("Enter the question:")

if question:
    response = llm.invoke(question)
    st.write(response.content)


