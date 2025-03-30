# AI-Powered Resume Screening and Ranking System

## ⭐ Overview
This project is an **AI-powered Resume Screening and Candidate Ranking System** built using **Streamlit** and **machine learning** techniques. It allows recruiters to automatically analyze and rank resumes based on their relevance to a given job description.

## 🚀 Features
- 📌 **Job Description Input**: Users can enter the job description manually.
- 📂 **Resume Upload**: Supports uploading multiple **PDF resumes**.
- 🔍 **AI-Powered Analysis**:
  - **TF-IDF-based ranking** for relevance.
  - **Skill matching** against predefined technical skills.
  - **ATS Score Calculation** for resume optimization.
- 📊 **Visualization & Insights**:
  - Resume ranking based on AI analysis.
  - **ATS score distribution** via bar charts.
  - **AI-powered resume improvement suggestions**.
  - **Detailed extracted resume content display**.

## 🌍 Live Demo  
🚀 **Try it out here** → [AI-Powered Resume Screening](https://ai-powered-resume-screening.streamlit.app/)

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/ai-resume-screening.git
cd ai-resume-screening
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```bash
streamlit run app.py
```

## 📜 How It Works

1. **Enter Job Description**: Type in the job description in the text area.
2. **Upload Resumes**: Upload multiple PDF resumes.
3. **Click "Analyze Resumes"**: The system processes resumes and ranks them.
4. **View Results**: Get ranked resumes, ATS scores, skill matches, and improvement suggestions.

## 🛠️ Tech Stack
- **Python** (Streamlit, Pandas, Scikit-learn, PyPDF2, Regex)
- **Machine Learning** (TF-IDF Vectorization, Cosine Similarity)

## 📊 AI Resume Ranking Algorithm
- **TF-IDF Vectorization**: Converts job description and resumes into numerical vectors.
- **Cosine Similarity**: Measures textual similarity between job description and resumes.
- **Skill Matching**: Extracts and compares skills from resumes and job descriptions.
- **ATS Scoring**: Evaluates resume formatting and keyword density.

## 📌 To-Do
- ✅ Add more predefined skills for better matching.
- ✅ Improve ATS scoring algorithm.
- ⏳ Integrate NLP for better resume parsing.
- ⏳ Deploy to a cloud service (e.g., AWS, Heroku).

## 🤝 Contributing
Pull requests are welcome! Feel free to fork the repository and submit improvements.

