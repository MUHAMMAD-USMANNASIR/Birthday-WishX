# birthday_wisher.py
import streamlit as st
import requests

# Hugging Face API setup
import os

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct"
headers = {"Authorization": f"Bearer {os.environ['HF_API_KEY']}"}

def generate_wish(name):
    prompt = f"Write a heartfelt and elegant birthday wish for {name}. Make it positive, inspiring, and warm."
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    try:
        return response.json()[0]['generated_text']
    except:
        return f"Happy Birthday {name}! Wishing you joy, success, and beautiful moments ahead."

# Streamlit Page Config
st.set_page_config(page_title="Birthday Wisher", layout="centered")

# Custom CSS for aesthetics
st.markdown(
    """
    <style>
    body {
        background-color: #f9f9f9;
        color: #222222;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stButton>button {
        background: linear-gradient(to right, #6a11cb, #2575fc);
        color: white;
        border: none;
        padding: 0.6em 1.2em;
        border-radius: 10px;
        font-size: 16px;
        font-weight: 500;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(to right, #2575fc, #6a11cb);
    }
    .wish-box {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        margin-top: 20px;
        font-size: 18px;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Layout
st.title("Birthday Wisher")
st.write("Generate an elegant and personalized birthday wish.")

name = st.text_input("Enter a name:")

if st.button("Generate Wish"):
    if name.strip():
        with st.spinner("Creating a beautiful wish..."):
            wish = generate_wish(name.strip())
        st.markdown(f"<div class='wish-box'>{wish}</div>", unsafe_allow_html=True)
    else:
        st.warning("Please enter a name first.")
