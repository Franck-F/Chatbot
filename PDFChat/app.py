import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

#Sidebar contents
with st.sidebar:
    st.title("LLM Chat_App")
    st.markdown('''
                ## About
                This is a simple chat application using Large Language Models (LLMs) like LLaMA,
                BERT, RoBERTa, etc. It uses the Hugging Face Transformers library to handl,
                the LLMs. The application is built using Streamlit, a Python library for building
                - [Streamlit](https://streamlit.io/)
                - [LangChain](https://www.langchain.com/)
                - [OpenAI](https://openai.com/)
                ''')
    add_vertical_space(5)
    st.write('Made by Franck Fambou')