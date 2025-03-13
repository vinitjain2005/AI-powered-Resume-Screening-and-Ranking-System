import streamlit as st
import base64
import pandas as pd
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Set page configuration for a wide layout
st.set_page_config(page_title="AI Resume Screening", layout="wide")

st.markdown("""
# AI Resume Screening and Candidate Ranking System

Welcome to the interactive resume screening tool.  
**Steps to follow:**
1. Enter the job description.
2. Upload resume PDFs.
3. Click **Analyze Resumes** to view ranking results, visualizations, and detailed resume text.
""")

# Input for job description
st.header("Job Description")
job_description = st.text_area("Enter the job description", height=200)

# File uploader for PDF resumes
st.header("Upload Resumes")
uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

# Button to trigger the analysis
if st.button("Analyze Resumes"):
    # Validate inputs
    if not job_description.strip():
        st.error("Please enter a job description.")
    elif not uploaded_files:
        st.error("Please upload at least one PDF resume.")
    else:
        st.header("Processing Resumes")
        resumes = []
        progress_bar = st.progress(0)
        
        # Extract text from each PDF and update progress
        for i, file in enumerate(uploaded_files):
            pdf = PdfReader(file)
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
            resumes.append(text)
            progress_bar.progress((i + 1) / len(uploaded_files))
        
        st.success("Text extraction complete!")
        
        # Compute ranking scores
        documents = [job_description] + resumes
        vectorizer = TfidfVectorizer().fit_transform(documents)
        vectors = vectorizer.toarray()
        job_description_vector = vectors[0]
        resume_vectors = vectors[1:]
        scores = cosine_similarity([job_description_vector], resume_vectors).flatten()
        
        results = pd.DataFrame({
            'Resume': [file.name for file in uploaded_files],
            'Score (%)': [round(score * 100, 2) for score in scores]
        }).sort_values(by="Score (%)", ascending=False)
        
        # Function to create a CSV download link
        def get_table_download_link(df):
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()  # Encode CSV to base64
            return f'<a href="data:file/csv;base64,{b64}" download="resume_ranking.csv">Download CSV File</a>'
        
        # Organize results using tabs
        tab1, tab2, tab3 = st.tabs(["Results", "Visualization", "Resume Details"])
        
        with tab1:
            st.subheader("Ranking Results")
            st.write(results)
            st.markdown(get_table_download_link(results), unsafe_allow_html=True)
        
        with tab2:
            st.subheader("Score Distribution")
            st.bar_chart(results.set_index("Resume"))
            
        with tab3:
            st.subheader("Detailed Resume Text")
            for i, file in enumerate(uploaded_files):
                with st.expander(f"{file.name} - Score: {round(scores[i] * 100, 2)}%"):
                    st.write(resumes[i])
