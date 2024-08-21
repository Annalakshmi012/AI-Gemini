import streamlit as st
import google.generativeai as genai

st.title("Welcome to My GPT")

genai.configure(api_key="AIzaSyDhJr8tVK8Sq27bL38O0PYtUSe9J1bs5XA")

text =st.text_input("Enter a Question:")

model = genai.GenerativeModel('gemini-pro')

chat=model.start_chat(history=[])

response =chat.send_message(text)

st.write(response.text)