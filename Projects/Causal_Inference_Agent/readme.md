# 🧠 Causal Inference Agent – Humanitarians AI

## 📌 Project Overview
The **Causal Inference Agent** is an AI-powered application that enables users to upload healthcare datasets and ask natural language questions about causal relationships (e.g., “What is the effect of medication X on recovery?”). The system uses LLMs (like Groq) to infer variables, preprocess the data, and run statistical causal analysis using techniques such as **propensity score matching**.

This tool allows health researchers, hospitals, and policymakers to gain insights into treatment efficacy and healthcare outcomes — without needing deep statistical knowledge.

---

## 🚀 Features
- **Streamlit Web UI**: Upload CSVs and type in natural language questions.
- **LLM Variable Detection**: Automatically detects treatment, outcome, and covariates using Groq LLM.
- **Causal Alignment & Preprocessing**: Auto-aligns and binarizes variables for analysis.
- **Sampling for Performance**: Optimized for large datasets with class-balanced sampling.
- **FastAPI Backend**: Supports programmatic access via REST API for batch analysis.
- **Statistical Reporting**: Effect size, confidence interval, p-value, and plain English summary.

---

## 🧪 Example Causal Questions (from `input.txt`)
1. *What is the causal effect of prescribing Ibuprofen on producing normal test results?*
2. *Does the type of admission (Emergency vs Elective) impact recovery outcomes?*
3. *Does the insurance provider influence the billing amount charged?*

---

## 🛠️ Technologies Used
- **Frontend**: Streamlit
- **Backend**: FastAPI
- **LLM**: Groq Llama3 via OpenAI-compatible API
- **Data Analysis**: Pandas, scikit-learn, statsmodels
- **Deployment**: Uvicorn (dev server), `.env` for API key management

---

## 📂 Project Structure
├── app1.py # Streamlit UI ├── main.py # FastAPI backend ├── groq_api.py # Interface to Groq LLM ├── utils.py # Preprocessing, binarization, validation ├── config.py # Config management with .env support ├── requirements.txt # Dependencies ├── input.txt # Sample questions and schema mapping


## 🌍 Contribution to Humanitarians AI
This module contributes toward Humanitarians AI's mission by:
- Empowering low-resource hospitals and NGOs to make **data-driven medical decisions**.
- Providing **explainable causal insights** that support better treatment planning.
- Reducing the barrier to statistical analysis using **natural language inputs**.

---

## 👩‍💻 Author
Mrinalini Suresh Jadhav  
📧 [your.email@example.com]  
🔗 [LinkedIn/GitHub if applicable]

---

> 📌 **Reminder:** No code is included here. For demo or source code, reach out via email.