# IMPORTS
import pandas as pd
import streamlit as st
from PIL import Image

# Custom CSS Styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Oswald&display=swap');

    /* Background and Font */
    html, body, .main, .block-container {
        background-color: #423d4c !important;
        color: #DDDDDD !important;
        font-family: 'Oswald', sans-serif;
    }

    /* Make All Text White */
    h2, h3, h4, h5, h6, p, span {
        color: #DDDDDD !important;
    }

    /* Make Main Title Blue */
    h1 {
        color: #007AFF !important;
        text-align: center;
        margin-top: 0px;
        margin-bottom: 10px;
        font-size: 48px;
    }

    /* Smooth Background for Containers */
    section[data-testid="stSidebar"], section[data-testid="stMain"] {
        background-color: #423d4c !important;
    }

    /* Only target the Candidate Search box */
    div[data-testid="stTextInput"] label:contains("Search by Candidate Name or Skill") div input {
    color: black !important;
}


    /* Add soft shadow to inputs */
    input, textarea, .stSelectbox, .stTextInput {
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    }

    /* Tighten Dropdown Margin */
    div[data-testid="stSelectbox"] {
        margin-top: -10px;
    }

    /* Make selected dropdown text black */
    section[data-testid="stSelectbox"] div[data-baseweb="select"] > div > div {
          color: black !important;
     }

    /* Fix Slider Labels (0, 100) */
    div[data-testid="stSlider"] .css-1k0ckh2 {
        color: white !important;
    }

    /* Download Button */
    .stDownloadButton > button {
        background-color: #007AFF !important;
        color: white !important;
        border: none;
        padding: 0.5em 1em;
        font-size: 1em;
        font-weight: bold;
        border-radius: 8px;
    }

    /* Download Button Hover */
    .stDownloadButton > button:hover {
        background-color: #005bb5 !important;
    }

    /* Footer */
    footer {
        visibility: hidden;
    }

    footer:after {
        content: 'Built for Shift Group by Cassidy Ward - 2025';
        visibility: visible;
        display: block;
        text-align: center;
        color: white;
        padding: 10px;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# BRANDING SECTION

logo = Image.open('../assets/shiftgroup_logo.webp')
st.image(logo, width=200)

st.markdown(
     """
     <h1 style='text-align: center; color: #007AFF; font-size: 48px;'> Shift Group Matching Engine</h1>
     <p style='text-align: center; color: #DDDDDD; font-size: 18px;'>
          This internal tool matches candidates to open roles based on  skill alignment, experience, and location fit - built to scale Shift Group's placement process.
     </p>
     """,
     unsafe_allow_html=True
)

# Load strong matches file
matches_df = pd.read_csv('../data/strong_candidate_job_matches.csv')

# Dropdown to select a job
job_options = matches_df["job_id"].unique()
selected_job = st.selectbox("Select a Job to See Top Matches:", job_options)

# Match score threshold filter
min_score = st.slider("Minimum Match Score (%)", 0, 100, 60)
search_term = st.text_input("Search by Candidate Name or Skill")

# Apply all filters
job_matches = matches_df[
     (matches_df["job_id"] == selected_job) & 
     (matches_df["match_score"] * 100 >= min_score)
]

# Optional text search filter
if search_term:
     job_matches = job_matches[
          job_matches["candidate_id"].str.contains(search_term, case=False, na=False) |
          job_matches["candidate_skills"].str.contains(search_term, case=False, na=False)
     ]

# Display matches
st.subheader(f"Top Candidates for Job {selected_job} (>= {min_score}%)")
st.dataframe(
    job_matches[["candidate_id", "match_score_pct", "candidate_skills", "candidate_location"]]
)

# Download button for filtered job matches 
csv = job_matches.to_csv(index=False).encode('utf-8')
st.download_button(
     label="Download this match table as CSV",
     data=csv,
     file_name=f'matches_for_{selected_job}.csv',
     mime='text/csv'
)

st.caption("Prototype built for Shift Group demo.")

