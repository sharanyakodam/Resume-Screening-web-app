# Resume Screening App with Internship Job Links

This is a Streamlit-based web application that predicts the job category from a resume and recommends related internship job links.

## Features
- Upload a resume (PDF or TXT)
- Predicts the most relevant job category using a machine learning model
- Displays related internship job links for the predicted category

## Project Structure
- `app.py` – Main Streamlit app
- `.gitignore` – Excludes unnecessary files from version control
- `UpdatedResumeDataSet.csv` – (Optional) Example dataset (if included)
- `clf.pkl`, `tfidf_vectorizer.pkl`, `label_encoder.pkl` – Model and vectorizer files (if included)
- `resume.ipynb` – Jupyter notebook for data/model exploration (if included)

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/sharanyakodam/Resume-Screening-web-app.git
   cd Resume-Screening-web-app
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install streamlit PyPDF2 nltk scikit-learn
   ```

4. **Download or place the following files in the project folder:**
   - `clf.pkl`, `tfidf_vectorizer.pkl`, `label_encoder.pkl`
   - (Optional) `UpdatedResumeDataSet.csv`, `resume.ipynb`

5. **Run the app:**
   ```sh
   streamlit run app.py
   ```

6. **Open the provided local URL in your browser (usually http://localhost:8501)**

---

## Notes
- Large files (like model `.pkl` or dataset `.csv`) are typically not stored in GitHub. If you want to share them, use Google Drive, Dropbox, or GitHub Releases, and provide a link here.
- To upload all files (including those in `.gitignore`), see the instructions below.

---

## How to Upload All Files to GitHub (not recommended for large files)

1. **Edit `.gitignore`:**
   - Remove or comment out lines that match files you want to include (e.g., `*.csv`, `*.pkl`, `*.ipynb`, `venv/`).

2. **Add and commit all files:**
   ```sh
   git add .
   git commit -m "Add all files"
   git push
   ```

3. **If you only want to force add specific files:**
   ```sh
   git add -f UpdatedResumeDataSet.csv resume.ipynb clf.pkl tfidf_vectorizer.pkl
   git commit -m "Add data and model files"
   git push
   ```

**Warning:** Uploading large files or virtual environments to GitHub is not recommended. Use cloud storage for sharing large data/model files.

---

## License
This project is for educational purposes.
