import streamlit as st
import pickle
import re
import nltk
from PyPDF2 import PdfReader  # make sure PyPDF2 is installed

nltk.download('punkt')
nltk.download('stopwords')

# Load your model and vectorizer
clf = pickle.load(open('clf.pkl', 'rb'))
tfidfd = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))

category_map = {
    1: "Arts",
    7: "Database",
    11: "Electrical Engineering",
    14: "Health and fitness",
    19: "PMO",
    4: "Business Analyst",
    9: "DotNet Developer",
    2: "Automation Testing",
    17: "Network Security Engineer",
    21: "SAP Developer",
    5: "Civil Engineer",
    0: "Advocate",
    15: "Java Developer",
    23: "Testing",
    8: "DevOps Engineer",
    20: "Python Developer",
    24: "Web Designing",
    12: "HR",
    13: "Hadoop",
    3: "Blockchain",
    10: "ETL Developer",
    18: "Operations Manager",
    6: "Data Science",
    22: "Sales",
    16: "Mechanical Engineer"
}

# Internship links for each category
internship_links = {
    "Arts": [
        "https://www.indeed.com/q-arts-internship-jobs.html",
        "https://internshala.com/internships/arts-internship/"
    ],
    "Database": [
        "https://www.indeed.com/q-database-internship-jobs.html",
        "https://internshala.com/internships/database-internship/"
    ],
    "Electrical Engineering": [
        "https://www.indeed.com/q-electrical-engineering-internship-jobs.html",
        "https://internshala.com/internships/electrical-engineering-internship/"
    ],
    "Health and fitness": [
        "https://www.indeed.com/q-health-fitness-internship-jobs.html",
        "https://internshala.com/internships/health-and-fitness-internship/"
    ],
    "PMO": [
        "https://www.indeed.com/q-pmo-internship-jobs.html",
        "https://internshala.com/internships/pmo-internship/"
    ],
    "Business Analyst": [
        "https://www.indeed.com/q-business-analyst-internship-jobs.html",
        "https://internshala.com/internships/business-analyst-internship/"
    ],
    "DotNet Developer": [
        "https://www.indeed.com/q-dotnet-internship-jobs.html",
        "https://internshala.com/internships/dotnet-internship/"
    ],
    "Automation Testing": [
        "https://www.indeed.com/q-automation-testing-internship-jobs.html",
        "https://internshala.com/internships/automation-testing-internship/"
    ],
    "Network Security Engineer": [
        "https://www.indeed.com/q-network-security-internship-jobs.html",
        "https://internshala.com/internships/network-security-internship/"
    ],
    "SAP Developer": [
        "https://www.indeed.com/q-sap-internship-jobs.html",
        "https://internshala.com/internships/sap-internship/"
    ],
    "Civil Engineer": [
        "https://www.indeed.com/q-civil-engineering-internship-jobs.html",
        "https://internshala.com/internships/civil-engineering-internship/"
    ],
    "Advocate": [
        "https://www.indeed.com/q-legal-internship-jobs.html",
        "https://internshala.com/internships/law-internship/"
    ],
    "Java Developer": [
        "https://www.indeed.com/q-java-internship-jobs.html",
        "https://internshala.com/internships/java-internship/"
    ],
    "Testing": [
        "https://www.indeed.com/q-testing-internship-jobs.html",
        "https://internshala.com/internships/testing-internship/"
    ],
    "DevOps Engineer": [
        "https://www.indeed.com/q-devops-internship-jobs.html",
        "https://internshala.com/internships/devops-internship/"
    ],
    "Python Developer": [
        "https://www.indeed.com/q-python-internship-jobs.html",
        "https://internshala.com/internships/python-internship/"
    ],
    "Web Designing": [
        "https://www.indeed.com/q-web-design-internship-jobs.html",
        "https://internshala.com/internships/web-design-internship/"
    ],
    "HR": [
        "https://www.indeed.com/q-hr-internship-jobs.html",
        "https://internshala.com/internships/hr-internship/"
    ],
    "Hadoop": [
        "https://www.indeed.com/q-hadoop-internship-jobs.html",
        "https://internshala.com/internships/hadoop-internship/"
    ],
    "Blockchain": [
        "https://www.indeed.com/q-blockchain-internship-jobs.html",
        "https://internshala.com/internships/blockchain-internship/"
    ],
    "ETL Developer": [
        "https://www.indeed.com/q-etl-internship-jobs.html",
        "https://internshala.com/internships/etl-internship/"
    ],
    "Operations Manager": [
        "https://www.indeed.com/q-operations-internship-jobs.html",
        "https://internshala.com/internships/operations-internship/"
    ],
    "Data Science": [
        "https://www.indeed.com/q-data-science-internship-jobs.html",
        "https://internshala.com/internships/data-science-internship/"
    ],
    "Sales": [
        "https://www.indeed.com/q-sales-internship-jobs.html",
        "https://internshala.com/internships/sales-internship/"
    ],
    "Mechanical Engineer": [
        "https://www.indeed.com/q-mechanical-engineering-internship-jobs.html",
        "https://internshala.com/internships/mechanical-engineering-internship/"
    ],
    "Unknown Category": [
        "https://www.indeed.com/q-internship-jobs.html",
        "https://internshala.com/internships/"
    ]
}

def clean_resume(txt):
    txt = re.sub(r'http\S+|www\S+', '', txt)
    txt = re.sub(r'\S+@\S+', '', txt)
    txt = re.sub(r'[^A-Za-z\s]', '', txt)
    txt = re.sub(r'^#.*$', '', txt)
    txt = re.sub(r'\s+', ' ', txt).strip()
    return txt

def main():
    st.title("📄 Resume Screening App")

    upload_file = st.file_uploader("Upload Resume (txt or pdf)", type=['txt', 'pdf'])

    if upload_file is not None:
        try:
            if upload_file.type == "application/pdf":
                pdf_reader = PdfReader(upload_file)
                resume_text = ""
                for page in pdf_reader.pages:
                    resume_text += page.extract_text()
            else:
                resume_text = upload_file.read().decode('utf-8')
        except Exception as e:
            st.error(f"Error reading file: {e}")
            return

        cleaned_text = clean_resume(resume_text)
        input_features = tfidfd.transform([cleaned_text])
        prediction_id = clf.predict(input_features)[0]
        category_name = category_map.get(prediction_id, "Unknown Category")

        st.write(f"**Predicted Category Name:** {category_name}")

        # Show related internship job links
        st.markdown("\n**Related Internship Job Links:**")
        links = internship_links.get(category_name, internship_links["Unknown Category"])
        for url in links:
            st.markdown(f"- [View Internship]({url})")

if __name__ == "__main__":
    main()
