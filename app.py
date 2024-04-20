from dotenv import load_dotenv

load_dotenv()

import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_PRO_API"))

## function to load Gemini Pro Model and get response

model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

## initialize streamlit app

st.set_page_config(page_title="Q&A Chatbot")

st.header("Gemini Pro LLM Application")

input = st.text_input("Input: ", key="input")

submit = st.button("Ask the question....")

## When Submit is Clicked

if submit:
    response=get_gemini_response(input)
    st.subheader("The Response is : ")
    st.write(response)