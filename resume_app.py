import streamlit as st
import base64
import pandas as pd
import re
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Set page configuration
st.set_page_config(page_title="⭐ AI Resume Screening ⭐", layout="wide")

st.markdown("""
# 🏆 AI Resume Screening and Candidate Ranking System

Welcome to the interactive resume screening tool. 🚀

**📌 Steps to follow:**
1. 📝 Enter the job description.
2. 📂 Upload resume PDFs.
3. 🔍 Click **Analyze Resumes** to view ranking results and ATS score.
""")

# Input for job description
st.header("📄 Job Description")
job_description = st.text_area("📝 Enter the job description", height=200)

# File uploader for PDF resumes
st.header("📂 Upload Resumes")
uploaded_files = st.file_uploader("📥 Upload PDF files", type=["pdf"], accept_multiple_files=True)

def preprocess_text(text):
    """Clean text by keeping important terms and removing unnecessary special characters."""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s.,]', '', text)  # Keep periods and commas for context
    return text


def extract_skills(text):
    """Extract relevant skills from the text based on a predefined skill set."""
    skills_set = {"python", "java", "sql", "data analysis", "machine learning", "excel", "power bi", "tensorflow", "pytorch", "cloud", "aws", "security", "blockchain", "react", "nodejs", "mongodb"}
    words = set(text.split())
    matched_skills = skills_set.intersection(words)
    return matched_skills

def calculate_ats_score(text):
    """Calculate ATS score based on formatting, keyword density, and structure."""
    section_headers = ["education", "skills", "experience", "projects", "certifications"]
    section_count = sum(1 for header in section_headers if header in text)
    bullet_points = text.count("•") + text.count("-")
    keyword_density = len(extract_skills(text)) / max(1, len(text.split()))
    ats_score = (section_count * 15) + (bullet_points * 2) + (keyword_density * 40)
    return min(100, max(1, round(ats_score)))

def suggest_improvements(text):
    """Provide AI-generated suggestions for resume improvement."""
    improvements = []
    if "education" not in text:
        improvements.append("Add an 'Education' section to highlight your academic background.")
    if "skills" not in text:
        improvements.append("Include a 'Skills' section with relevant keywords matching the job description.")
    if "experience" not in text:
        improvements.append("List your work experience with clear job titles and responsibilities.")
    if "projects" not in text:
        improvements.append("Showcase key projects demonstrating your practical expertise.")
    if "certifications" not in text:
        improvements.append("Mention certifications relevant to the job role for an added advantage.")
    if len(improvements) == 0:
        improvements.append("Your resume is well-structured! Consider optimizing it further with strong action verbs and measurable achievements.")
    return improvements


if st.button("📊 Analyze Resumes"):
    if not job_description.strip():
        st.error("⚠️ Please enter a job description.")
    elif not uploaded_files:
        st.error("⚠️ Please upload at least one PDF resume.")
    else:
        st.subheader("⏳ Processing Resumes")
        resumes = []
        ats_scores = []
        progress_bar = st.progress(0)
        
        for i, file in enumerate(uploaded_files):
            pdf = PdfReader(file)
            text = "".join(page.extract_text() or "" for page in pdf.pages)
            text = preprocess_text(text)
            resumes.append(text)
            ats_scores.append(calculate_ats_score(text))
            progress_bar.progress((i + 1) / len(uploaded_files))
        
        st.success("✅ Text extraction complete!")
        
        processed_job_desc = preprocess_text(job_description)
        documents = [processed_job_desc] + resumes
        vectorizer = TfidfVectorizer().fit_transform(documents)
        vectors = vectorizer.toarray()
        job_vector = vectors[0]
        resume_vectors = vectors[1:]
        tfidf_scores = cosine_similarity([job_vector], resume_vectors).flatten()
        
        job_skills = extract_skills(job_description)
        resume_skills = [extract_skills(res) for res in resumes]
        skill_match_scores = [len(skills & job_skills) / max(1, len(job_skills)) for skills in resume_skills]
        
        final_scores = [max(1, min(100, round(((0.7 * tfidf) + (0.3 * skill)) * 100))) for tfidf, skill in zip(tfidf_scores, skill_match_scores)]
        
        results = pd.DataFrame({
            '📜 Resume': [file.name for file in uploaded_files],
            '🏆 Final Fit Score (%)': [f"{score}%" for score in final_scores],
            '📊 ATS Score (%)': [f"{score}%" for score in ats_scores]
        }).sort_values(by="🏆 Final Fit Score (%)", ascending=False)
        
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏅 Results", "📊 ATS Score", "✨ AI Improvements", "📄 Resume Details", "🔍 Skill Matching"])
        
        with tab1:
            st.subheader("🏅 Ranking Results")
            st.dataframe(results, height=300)
        
        with tab2:
            st.subheader("📊 ATS Score Distribution")
            st.bar_chart(results.set_index("📜 Resume"))
        
        with tab3:
            st.subheader("✨ AI Improvement Suggestions")
            for i, file in enumerate(uploaded_files):
                with st.expander(f"{file.name} - Suggested Improvements"):
                    for suggestion in suggest_improvements(resumes[i]):
                        st.write(f"✅ {suggestion}")
        
        with tab4:
            st.subheader("📄 Detailed Resume Text")
            for i, file in enumerate(uploaded_files):
                with st.expander(f"{file.name} - 🏆 Score: {final_scores[i]}% | 📊 ATS Score: {ats_scores[i]}%"):
                    st.write(resumes[i])
        
        with tab5:
            st.subheader("🔍 Skill Matching Details")
            for i, file in enumerate(uploaded_files):
                with st.expander(f"{file.name} - ✅ Matched Skills: {', '.join(resume_skills[i])}"):
                    st.write(f"📝 Job Required Skills: {', '.join(job_skills)}")
                    st.write(f"🔹 Matched Skills: {', '.join(resume_skills[i])}")