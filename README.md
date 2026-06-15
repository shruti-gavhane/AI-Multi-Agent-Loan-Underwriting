# 🚀 Multi-Agent Loan Approval System

An AI-powered multi-agent loan approval and underwriting system built using **LangGraph**, **FastAPI**, **Streamlit**, **SQLite**, and **LLMs** to automate customer verification, sales consultation, underwriting evaluation, risk analysis, EMI calculation, and sanction letter generation.

This project simulates a real-world financial institution’s loan processing pipeline by using multiple specialized agents that collaborate to make explainable and structured lending decisions.

---

# 📌 Problem Statement

Traditional loan approval systems face several challenges:

- Manual verification is slow and inefficient
- Underwriting lacks consistency
- Risk evaluation is often delayed
- Sales qualification is disconnected from underwriting
- Decision transparency is poor

Banks and financial institutions need:

✔ Faster loan application processing  
✔ Automated applicant verification  
✔ Better underwriting consistency  
✔ Dynamic EMI calculation  
✔ Risk-based approval logic  
✔ Automated sanction letter generation  
✔ Centralized application storage  

This project solves these problems using a multi-agent architecture.

---

# 🏗️ System Architecture

## Workflow Diagram

```text
Customer Application
        │
        ▼
Sales Agent
(Collects applicant info)
        │
        ▼
Verification Agent
(Validates applicant data)
        │
        ▼
Underwriting Agent
(Analyzes loan eligibility)
        │
        ▼
Risk Agent
(Assigns risk level)
        │
        ▼
Decision Engine
(Approve / Reject)
        │
        ▼
PDF Generator
(Sanction Letter)
        │
        ▼
SQLite Database Storage
```

---

# 🤖 Agent Architecture

```text
                   Loan Application
                           │
                           ▼
                ┌────────────────────┐
                │   LangGraph Flow   │
                └────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
   Sales Agent      Verification Agent   Underwriting Agent
                                                │
                                                ▼
                                           Risk Agent
                                                │
                                                ▼
                                         Final Decision
                                                │
                                                ▼
                                      Sanction Letter Generator
```

---

# 📂 Project Structure

```text
MULTI-AGENT-LOAN-APPROVAL-AI-SYSTEM/

├── agents/
│   ├── risk_agent.py
│   ├── sales_agent.py
│   ├── underwriting_agent.py
│   └── verification_agent.py
│
├── services/
│   ├── external_data.py
│   ├── llm_service.py
│   └── repository.py
│
├── utils/
│   ├── emi_calculator.py
│   └── pdf_generator.py
│
├── graph_builder.py
├── init_db.py
├── loan.db
├── main.py
├── schemas.py
├── streamlit_app.py
├── requirements.txt
├── .env
└── README.md
```

---

# 🛠 Tech Stack

## Backend

- Python
- FastAPI
- LangGraph
- SQLite

## Frontend

- Streamlit

## AI/LLM

- LangChain
- Groq API
- OpenRouter API
- Together AI

## Utilities

- ReportLab (PDF Generation)
- Custom EMI Calculator

---

# ✨ Features

## 📞 Sales Agent

Responsible for:

- Collecting applicant information
- Initial lead qualification
- Loan requirement understanding
- Customer onboarding

---

## ✅ Verification Agent

Performs:

- Identity verification
- Contact verification
- Data validation
- Document consistency checks

---

## 📝 Underwriting Agent

Handles:

- Loan eligibility analysis
- Income evaluation
- Debt assessment
- Repayment capability analysis
- Approval recommendation

---

## ⚠️ Risk Agent

Evaluates:

- Applicant risk profile
- Financial stability
- Loan repayment risk
- Risk categorization

Risk levels:

- Low Risk
- Medium Risk
- High Risk

---

## 💸 EMI Calculator

Calculates:

- Monthly EMI
- Total payable amount
- Interest amount
- Loan repayment schedule

---

## 📄 PDF Sanction Letter Generator

Generates:

- Loan approval letter
- Loan rejection letter
- Loan terms summary

---

## 🗄 Database Storage

Stores:

- Applicant details
- Loan status
- Risk category
- Underwriting results
- Approval history

---
---

## 1. Loan Application Form

```text
![Loan Form](https://github.com/user-attachments/assets/968f8cbb-1ef4-4aad-ac23-7c540144f346)
```
---

## 2. Loan Decision Output

```text
<img width="1893" height="767" alt="Screenshot 2026-06-15 225254" src="https://github.com/user-attachments/assets/57304897-ccd4-4cb3-91e1-6b3a17529cf6" />
<img width="1817" height="591" alt="Screenshot 2026-06-15 225320" src="https://github.com/user-attachments/assets/e6da8f3d-e487-4ca1-b21e-059e8397c5b4" />
<img width="1876" height="791" alt="Screenshot 2026-06-15 225354" src="https://github.com/user-attachments/assets/c1af9733-36b7-494f-9cd6-f789a6b216cc" />

```

---
## 3. Loan Decision Chatbot

```text
<img width="1892" height="627" alt="image" src="https://github.com/user-attachments/assets/6d19177b-5dde-451f-9457-90f08c71ac84" />
```

---
## 4. Generated Sanction Letter PDF

```text
<img width="1878" height="831" alt="image" src="https://github.com/user-attachments/assets/102556a9-a56c-4bfa-be76-8bd408bd7f5b" />

```
---
# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/multi-agent-loan-approval-ai-system.git

cd multi-agent-loan-approval-ai-system
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Setup Environment Variables

Create `.env`

```env
GROQ_API_KEY=your_key

OPENROUTER_API_KEY=your_key

TOGETHER_API_KEY=your_key
```

---

## Initialize Database

```bash
python init_db.py
```

---

## Run FastAPI Server

```bash
uvicorn main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

---

## Run Streamlit Frontend

```bash
streamlit run streamlit_app.py
```

---

# 🔌 API Endpoints

## Submit Loan Application

```http
POST /apply-loan
```

---

## Get Loan Status

```http
GET /loan-status/{id}
```

---

## Generate Sanction Letter

```http
POST /generate-sanction-letter
```

---

## Calculate EMI

```http
POST /calculate-emi
```

---

# 🗄 Database Schema

## Loan Applications Table

| Field | Type |
|---|---|
| id | INTEGER |
| applicant_name | TEXT |
| income | REAL |
| loan_amount | REAL |
| tenure | INTEGER |
| risk_level | TEXT |
| approval_status | TEXT |

---

# 🔄 Agent Flow

```text
START

 ↓

Sales Agent

 ↓

Verification Agent

 ↓

Underwriting Agent

 ↓

Risk Agent

 ↓

EMI Calculation

 ↓

Decision Generation

 ↓

PDF Generation

 ↓

Database Storage

 ↓

END
```

---

# 📈 Future Improvements

- OCR-based document verification
- Bank statement analysis
- Credit bureau integration
- Aadhaar/PAN verification
- Fraud detection model
- Multi-bank policy engine
- Real-time market rate integration
- Human-in-the-loop approval
- RAG for loan policy retrieval
- Deployment on AWS/GCP
- Docker support

---

# 🎯 Key Highlights

✅ Multi-Agent Loan Processing Pipeline  
✅ LangGraph Workflow Orchestration  
✅ Automated Loan Underwriting  
✅ Explainable Approval Logic  
✅ Dynamic EMI Calculation  
✅ PDF Sanction Letter Generation  
✅ Streamlit Dashboard  
✅ SQLite Data Persistence  
✅ Production-ready FastAPI APIs  

---

# 👩‍💻 Author

### Shruti Gavhane

AI/ML Engineer | Full Stack Developer | Generative AI Enthusiast

**GitHub:** https://github.com/shruti-gavhane

**LinkedIn:** https://www.linkedin.com/in/shruti-gavhane-44994729a/

---

⭐ If you found this project useful, consider giving it a star!
