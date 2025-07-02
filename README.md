# 📊 Skill Demand Analyzer

A beautiful Streamlit web app that visualizes **in-demand technical skills** from job listings based on location.  
Perfect for data enthusiasts, job seekers, and career analysts!

![Banner](https://cdn-icons-png.flaticon.com/512/9046/9046845.png)

---

## 🚀 Features

- 📥 Upload a CSV of job postings (under 200MB)
- 🧠 Automatically extracts tech skills like `Python`, `SQL`, `Excel`, etc.
- 📍 Choose a city to see the top 10 skills in that location
- 📊 Interactive skill frequency bar chart
- ✨ Clean UI with animations using Streamlit + Lottie

---

## 🔧 Tech Stack

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Matplotlib](https://matplotlib.org/)
- [Pandas](https://pandas.pydata.org/)
- [Streamlit-Lottie](https://github.com/andfanilo/streamlit-lottie)

---

## 📂 File Structure

📁 skill-demand-analyzer/
├── app.py ← Streamlit app source code

├── requirements.txt ← Python dependencies

├── README.md ← Project info and usage guide

## 📥 Upload Your Own Dataset

Due to GitHub’s 100MB file upload limit, the dataset file `job_posting_cleaned.csv` is **not included** in this repository.

To use the app:
- Prepare your own CSV file
- It must contain at least these two columns:
  - `description` — the job description text
  - `location` — the city or region of the job posting

You can upload this file directly in the app after launching it.

Tip: Keep your file under 200MB to meet Streamlit Cloud limits.

---

## ⚙️ Installation & Running Locally

```bash
# Clone the repository
git clone https://github.com/your-username/skill-demand-analyzer.git
cd skill-demand-analyzer

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py

🌐 Live Demo

🙋‍♀️ Author
Made by Sreeya ks
