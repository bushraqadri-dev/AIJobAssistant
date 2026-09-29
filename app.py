import streamlit as st
from job_matcher import match_job
from resume_parser import extract_text_from_file

st.title("AI Job Application Assistant")

st.write("Analyze your resume against a job description.")

uploaded_resume = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

resume_text = ""

if uploaded_resume:
    resume_text = extract_text_from_file(uploaded_resume)

job_description = st.text_area(
    "Paste the job description here"
)

if st.button("Analyze Job Match"):

    if resume_text and job_description:

        match_percentage, required_skills, matched_skills, missing_skills = match_job(
            resume_text,
            job_description
        )

        st.subheader("📊 Job Match Result")

        st.metric(
            label="Resume Match",
            value=f"{match_percentage:.1f}%"
        )

        st.progress(int(match_percentage) / 100)
st.write("### 📌 Required Skills")

if required_skills:
            for skill in required_skills:
                st.info(skill)
else:
            st.info("No required skills detected.")

col1, col2 = st.columns(2)

with col1:
            st.markdown("### Matched Skills")

            if matched_skills:
                for skill in matched_skills:
                    st.success(skill)
            else:
                st.info("No matching skills found.")
with col2:
            st.markdown("### Missing Skills")

            if missing_skills:
                for skill in missing_skills:
                    st.warning(skill)
            else:
                st.success("No missing skills!")


                   
