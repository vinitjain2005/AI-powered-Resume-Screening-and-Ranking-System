# 🚀 AI-Powered Resume Screening and Ranking System

Welcome to the **AI-Powered Resume Screening and Ranking System**! This innovative tool leverages advanced Natural Language Processing techniques to help recruiters and HR professionals streamline the candidate evaluation process. By automatically screening and ranking resumes based on a job description, it saves time and ensures a more objective assessment of candidate fit.

Whether you're a recruiter looking to simplify your workload or a developer interested in AI-driven HR solutions, this project offers an intuitive and interactive way to filter through resumes and highlight top candidates.

## 🚀 How to Run the Project

1. **Clone or Download the Project Code:** 
   Obtain the project code from the repository.

2. **Navigate to the Project Directory in Your Terminal:**  
   Open VS Code’s integrated terminal and run:
   ```bash
   cd "C:\Users\YourUsername\Desktop\your_repo"

3. Run the Application Using Streamlit:
   You can start the app with one of the following commands:
   python -m streamlit run resume_app.py

   Alternatively, you can also run:
   streamlit run resume_app.py

4. Follow On-Screen Instructions:
   Enter the job description.
   Upload your PDF resumes.
   Click the Analyze Resumes button to view the results.


🔍 Detailed Step-by-Step Workflow
1. Job Description Input 📝
Purpose:
Provide a job description that details the skills, qualifications, and requirements for the position.
Usage:
Enter the description in the provided text area.
2. Uploading Resumes 📄
Purpose:
Upload one or more resume PDFs for screening.
Usage:
Use the file uploader to select PDF files from your system.
3. Processing & Ranking ⚙️
Text Extraction:
The application uses PyPDF2 to extract text from each PDF.
Similarity Calculation:
The text from resumes and the job description are converted to vectors using TF-IDF, and similarity is computed using cosine similarity.
4. Results Display 📊
Results Tab:
Displays a table of resume names and similarity scores (in percentage).
Visualization Tab:
A bar chart shows the score distribution.
Resume Details Tab:
Expandable sections display the full extracted text of each resume.
5. CSV Download 💾
Purpose:
Allows the user to download the ranking results for further analysis.
Usage:
Click the provided download link to save the results as a CSV file.

📌 Conclusion
This AI-powered resume screening tool aims to streamline the candidate evaluation process, making it more efficient and objective. Its interactive UI, combined with robust NLP techniques, helps recruiters quickly identify top candidates based on how well their resumes match the job description.
