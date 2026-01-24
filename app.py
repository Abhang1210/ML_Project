import streamlit as st
import pickle
import numpy as np
import sklearn

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("AI Resume Screening Tool")
st.write("Enter the required details to predict the suitability of a candidate.")

Years_experience = st.number_input("Years of Experience", min_value=0, max_value=50, value=1)

Skill_match_score = st.number_input("Skill Match Score (0-100)", min_value=0, max_value=100, value=50)

Projects_count = st.number_input("Number of Projects", min_value=0, max_value=100, value=1)

Resume_length = st.number_input("Resume Length (in pages)", min_value=1, max_value=20, value=1)

Github_activity = st.number_input("GitHub Activity Score (0-100)", min_value=0, max_value=100, value=50)

if st.button("Predict Suitability"):
    prediction = model.predict([[ 
        Years_experience,
        Skill_match_score,
        Projects_count,
        Resume_length,
        Github_activity
    ]])

    label_map = {
        "Yes": "Suitable",
        "No": "Not Suitable"
    }

    result = label_map[prediction[0]]

    if result == "Suitable":
        st.success(f"The candidate is **{result}**")
    else:
        st.error(f"The candidate is **{result}**")