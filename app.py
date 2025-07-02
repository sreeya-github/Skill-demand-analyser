import streamlit as st
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
import requests

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animation from Lottie URL
lottie_job = load_lottie_url("https://lottie.host/9df34568-d173-4c93-b9b6-6a12d55c3d5f/KK5BD2GGLO.json")
# PAGE SETTINGS
st.set_page_config(page_title="Skill Demand Analyzer", layout="wide", page_icon="📊")
st.image("https://cdn-icons-png.flaticon.com/512/9046/9046845.png", width=100)
# CUSTOM CSS FOR STYLING
st.markdown("""
    <style>
    /* Center title and add glow */
    .main > div:first-child { padding-top: 2rem; }
    h1 {
        font-size: 3.5em !important;
        text-align: center;
        color: #00b4d8;
        text-shadow: 1px 1px 2px black;
    }
    .stApp {
        background: linear-gradient(120deg, #f1f5f9, #dbeafe);
        font-family: 'Segoe UI', sans-serif;
    }
    .css-1d391kg { background-color: white !important; border-radius: 10px; padding: 1rem; }
    .css-1v0mbdj { font-size: 1.1em; }
    .css-ocqkz7 { color: #1d3557 !important; font-weight: 600; }
    .stButton>button {
        background-color: #00b4d8;
        color: white;
        font-weight: bold;
        padding: 0.5em 1em;
        border-radius: 10px;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #0077b6;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# TITLE
st.title("📊 Skill Demand Analyzer")
st.markdown("<h5 style='text-align:center;'>Discover which tech skills are most in-demand based on job location</h5>", unsafe_allow_html=True)

# UPLOAD FILE
uploaded_file = st.file_uploader("🔽 Upload Job Listings CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv("job_posting_cleaned.csv")

    # CHECK REQUIRED COLUMNS
    if 'description' not in df.columns or 'location' not in df.columns:
        st.error("❌ CSV must contain 'description' and 'location' columns.")
    else:
        # Define skills to extract
        skills_list = ['python', 'excel', 'sql', 'power bi', 'tableau', 'aws', 'r', 'machine learning']

        def extract_skills(text):
            text = str(text).lower()
            return [skill for skill in skills_list if skill in text]

        df['skills_found'] = df['description'].apply(extract_skills)
        df['location'] = df['location'].str.lower()

        city = st.selectbox("📍 Choose a Location", sorted(df['location'].dropna().unique()))

        filtered = df[df['location'] == city]

        st.subheader(f"📈 Top Skills in {city.title()}")

        all_skills = [skill for skills in filtered['skills_found'] for skill in skills]
        skill_counts = Counter(all_skills)

        if skill_counts:
            skills, counts = zip(*skill_counts.most_common(10))
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.barh(skills, counts, color='#0077b6')
            ax.set_xlabel("Number of Job Listings", fontsize=12)
            ax.set_title("Top 10 In-Demand Skills", fontsize=14)
            ax.invert_yaxis()
            ax.grid(True, axis='x', linestyle='--', alpha=0.5)
            st.pyplot(fig)
        else:
            st.warning("⚠️ No matching skills found for this location.")
else:
    st.info("👆 Please upload a CSV file to begin.")
