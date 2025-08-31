import streamlit as st
import random

# Predefined birthday wishes and quotes
wishes = [
    "Happy Birthday {name}, may your day be filled with joy and laughter.",
    "Wishing you a year ahead full of success, happiness, and love, {name}.",
    "{name}, may all your dreams come true this year. Have a wonderful birthday!",
    "Happy Birthday {name}! May your life be blessed with endless smiles and unforgettable moments.",
    "Cheers to you {name}, on your special day. May this year bring you closer to your goals."
]

quotes = [
    "“Count your age by friends, not years. Count your life by smiles, not tears.” – John Lennon",
    "“The more you praise and celebrate your life, the more there is in life to celebrate.” – Oprah Winfrey",
    "“Today you are you, that is truer than true. There is no one alive who is youer than you.” – Dr. Seuss",
    "“Every year on your birthday, you get a chance to start new.” – Sammy Hagar"
]

def generate_wish(name):
    wish = random.choice(wishes).format(name=name)
    quote = random.choice(quotes)
    return f"{wish}\n\n{quote}"

# Streamlit UI
st.set_page_config(page_title="Birthday Wisher", layout="centered")

# Custom Dark Mode Styling
st.markdown(
    """
    <style>
    body {
        background-color: #121212; /* Dark background */
        color: #f1f1f1; /* Light text */
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stButton>button {
        background: linear-gradient(to right, #ff416c, #ff4b2b); /* Pinkish gradient */
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
        background: linear-gradient(to right, #ff4b2b, #ff416c);
    }
    .wish-box {
        background: #1e1e1e; /* Dark card */
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.5);
        margin-top: 20px;
        font-size: 18px;
        line-height: 1.6;
        color: #f5f5f5; /* Light text inside card */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Layout
st.title("Birthday Wisher")
st.write("Generate a personalized and elegant birthday wish.")

name = st.text_input("Enter a name:")

if st.button("Generate Wish"):
    if name.strip():
        with st.spinner("Creating a beautiful wish..."):
            wish = generate_wish(name.strip())
        st.markdown(f"<div class='wish-box'>{wish}</div>", unsafe_allow_html=True)
    else:
        st.warning("Please enter a name first.")
