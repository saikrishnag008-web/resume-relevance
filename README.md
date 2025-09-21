# 🚀 Resume Relevance Checker

An AI-powered web application that automates resume evaluation against job descriptions, helping placement teams shortlist candidates faster, more consistently, and with actionable feedback.

## 🧠 Problem Statement

At Innomatics Research Labs, resume evaluation is manual, inconsistent, and time-consuming. Placement teams across Hyderabad, Bangalore, Pune, and Delhi NCR receive 18–20 job requirements weekly, each attracting thousands of applications. Manual screening leads to:

- ⏳ Delays in shortlisting
- 🤔 Inconsistent judgments
- 📉 Reduced focus on interview prep and student guidance

With hiring companies demanding fast and high-quality shortlists, there's a pressing need for a scalable, automated solution.

## 🎯 Objective

This system aims to:

- Automate resume evaluation at scale
- Generate a Relevance Score (0–100)
- Highlight missing skills, certifications, or projects
- Provide a suitability verdict (High / Medium / Low)
- Offer personalized feedback to students
- Store evaluations in a searchable dashboard for placement teams

## 🛠 Tech Stack

- *Frontend*: HTML, CSS (Glassmorphism, Gradients), JavaScript
- *Backend*: Python, FastAPI
- *Libraries*: PDFMiner, docx2txt
- *Design*: Font Awesome Icons, Animated UI, Responsive Layout

## 🧪 Approach

1. *Student Portal*:
   - Upload resume (PDF/DOCX)
   - Select job role (Frontend, Backend, Data Scientist)
   - Get instant relevance score, verdict, missing elements, and feedback

2. *Admin Portal*:
   - Secure login for placement team
   - Access dashboard with evaluation results

3. *Backend Logic*:
   - Extract text from resumes and job descriptions
   - Match keywords and compute relevance score
   - Return verdict and improvement suggestions

## 📦 Installation

### Prerequisites

- Python 3.8+
- Node.js (optional for frontend bundling)
- FastAPI & Uvicorn
- PDFMiner & docx2txt

### Setup

```bash
# Clone the repository
git clone https://github.com/your-username/resume-relevance-checker.git
cd resume-relevance-checker

# Install backend dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn main:app --reload
🧭 Usage
Student Portal
Open index.html in browser

Select job role

Upload resume

Click "Submit"

View:

✅ Relevance Score

📊 Verdict

❌ Missing Keywords

📝 Feedback

Admin Portal
Open admin.html

Login with:

Username: admin

Password: admin123

Redirects to dashboard (placeholder)

📂 Project Structure
Code
├── frontend/
│   ├── index.html
│   ├── admin.html
│   ├── style.css
│   ├── student.js
│   └── admin.js
├── backend/
│   ├── main.py
│   ├── utils/
│   │   ├── extract_text.py
│   │   └── evaluate.py
├── README.md
└── requirements.txt
💡 Future Enhancements
Integrate LLM-based semantic matching

Add dashboard analytics for recruiters

Role-based access control

Resume parsing with section-wise scoring

👨‍💻 Developed By
Team Cyber Punk | Hackathon 2025 Crafted with ❤ to make resume screening smarter, faster, and fairer