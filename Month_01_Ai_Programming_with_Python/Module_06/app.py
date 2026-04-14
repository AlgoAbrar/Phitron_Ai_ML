from google import genai 
import os 
from dotenv import load_dotenv
import streamlit as st 

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# api key should be secret

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Tell me about BAUET in 100 words" # we can take image, text input anything
)

#print(response.text)
st.markdown(response.text)