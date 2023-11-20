import openai
import streamlit as st

# step-back-prompting
# testen, ob name wirklich unterschied macht
# streamlit website anschauen
# chromadb anschauen
# max_tokens als limit setzen

file_path = "API_KEY"
openai.api_key = open(file_path, "r").read()

st.title("The app title")