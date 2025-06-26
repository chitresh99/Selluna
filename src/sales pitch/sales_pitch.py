import os
from dotenv import load_dotenv
from mistralai import Mistral
from system_prompt import system_prompt
import streamlit as st

st.set_page_config(page_title="Simple AI Chat", page_icon="🤖")
st.title("Sales pitch generator")

user = st.text_area("Your Query:",height=250)

load_dotenv()
api_key = os.getenv('mistral_api_key_new')
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

system = system_prompt()

def pitch_generator(prompt):
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
    )
    return chat_response.choices[0].message.content 

if user:
    ai_response = pitch_generator(user)
    st.text_area("AI Response:", value=ai_response, height=250, disabled=True)