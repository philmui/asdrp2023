##############################################################################
# Main script that builds the UI & connects the logic for an LLM-driven
# query frontend to an ASDRP demo app.
#
# @philmui
# Tue Jun 20 23:35:59 PDT 2023
##############################################################################

from transformers import pipeline
import streamlit as st
from pprint import pprint

##############################################################################

st.set_page_config(page_title="Translator", 
                   page_icon=":robot:", 
                   layout="wide")
st.header("🇫🇷🇪🇸 Translator 🇺🇸🇨🇳")

col1, col2 = st.columns([1,1])

with col1:
    option_llm = st.selectbox(
        "Model",
        (
            "Helsinki-NLP/opus-mt-fr-en",
            "Helsinki-NLP/opus-mt-en-fr",
            "Helsinki-NLP/opus-mt-es-en",
            "Helsinki-NLP/opus-mt-en-es",
            "Helsinki-NLP/opus-mt-it-en",
            "Helsinki-NLP/opus-mt-en-it",
            "Helsinki-NLP/opus-mt-en-de",
            "Helsinki-NLP/opus-mt-de-en",
        )
    )
with col2:
    pass

def get_query():
    input_text = st.text_area(label="Your input text", 
                              placeholder="Say anything",
                              key="question_text", label_visibility="collapsed")
    return input_text

query = get_query()

if query and len(query) > 1:
    output=""
    try:
        st.spinner(text="In progress...")
        translator = pipeline("translation", 
                              model=option_llm)
        output = translator(query)[0]['translation_text']
    except Exception as e:
        output=f"Sorry: cannot translate! {e}"
        
    height = min(2*len(output), 240)
    st.text_area(label="Response" , 
                 value=output, height=height)

