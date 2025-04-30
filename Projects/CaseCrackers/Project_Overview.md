# 📚 Case Crackers – AI-Powered Case-Study Practice & Interview Platform

[![Streamlit App – try it live!](https://img.shields.io/badge/Launch-CaseCrackers-green?logo=streamlit)](https://case-crackers.streamlit.app/)

*Case Crackers* is an end-to-end learning, assessment, and talent-matching platform that uses Generative AI to help students, professionals, and organisations **create, practise, and solve management case studies** faster than ever before.

---

## ✨ Key Features

| Module | What it does | Why it matters |
|--------|--------------|----------------|
| **Extensive Case Library** | Search a growing repository of real and user-generated cases across industries & difficulty levels | Democratises access to high-quality case material that is often expensive or restricted |
| **AI Case-Study Generator** | Choose *type → style → subject → difficulty* and instantly receive a bespoke case | Enables targeted, adaptive learning and supports interdisciplinary topics |
| **AI Interviewer Assistant** | Simulates interviewer- or candidate-led sessions and offers instant, structured feedback | Provides unlimited, realistic practice without scheduling human coaches |
| **Business-Solution Bot** | Upload a real business problem and get an AI-generated framework & recommendations (MATLAB LLM back-end) | Converts academic prototypes into actionable consulting output |
| **Interactive Dashboard** | Visualise usage stats, case popularity, difficulty trends, and learning curves | Helps educators and analysts track engagement and spot skill gaps |
| **Preparation Resources** | Curated reading lists, frameworks, glossaries & calculators | Everything you need for interview readiness in one place |

---

## 🌐 Live Demo  

👉 **Try it now:** <https://case-crackers.streamlit.app/>

---

## 🧠 Theoretical Foundation

1. **Experiential & Active Learning** – letting learners loop through *experience → reflection → theory → experimentation* on-demand.  
2. **Mastery Learning & Adaptive Difficulty** – difficulty settings and instant feedback enforce incremental mastery.  
3. **Cognitive-Load Management** – scaffolds reasoning (framework → numbers → synthesis) to minimise extraneous load.  
4. **Data-Driven Personalisation** – analytics surface skill gaps and schedule the next best case for each learner.  
5. **Democratisation of Professional Practice** – AI-generated and community-shared cases remove paywalls and promote equity.

---

## 🏗️ Tech Stack

| Layer     | Tools |
|-----------|-------|
| Front-End | **Streamlit** UI • `streamlit-extras` components |
| Core AI   | **OpenAI GPT-4o** for case generation and bot dialogue |
| Data      | Supabase for the case library • Pandas for analytics |
| Hosting   | Streamlit Community Cloud |

---

## 🗺️ Application Pages

### 1. Case Library

A searchable, filterable catalogue of every case (real & user-generated) with metadata such as industry, difficulty, creation date, and popularity. Use the sidebar filters or search bar to narrow results, then open a case for details or save it to your personal shortlist.

---

### 2. Case Generation

A form-based wizard where you pick *Case Type*, *Style*, *Difficulty*, and provide a short *Subject* prompt. Click **Generate Case** and the AI crafts a brand-new case plus interviewer notes. You can launch it directly into the Interview Bot or add it to the Library.

---

### 3. Case Interview Bot

A chat interface that mimics a live consulting interview. The transcript appears on the left; a scratchpad, timer, and scoring rubric sit on the right. Select a case, click **Start Interview**, and converse with the bot. When finished, download a detailed feedback report.

---

### 4. Business Solution Bot

Paste (or upload) a real business problem into a guided form. The bot analyses objectives, constraints, and context, then returns a MECE framework, risk assessment, and next-step recommendations you can export straight to PowerPoint.

---

### 5. Dashboard

Interactive charts (built with Plotly) display global and personal metrics: case popularity over time, success rates by difficulty, learning-curve heat maps, and competency gaps. Toggle filters (date range, industry, difficulty) and export visuals as PNG or CSV.

---

## 🕹️ Usage Guide

### Generate a Custom Case
1. **Select Case Type** – e.g. *Profitability*, *Market Entry*  
2. **Pick Style** – *Interviewer-led* or *Candidate-led*  
3. **Enter Subject** – a concise one-liner about the company/problem  
4. **Choose Difficulty** – *Easy / Medium / Hard*  
5. Click **Process** → your tailored case appears instantly.

### Practise with the AI Interviewer
1. Open the *Interview* tab and select a case.  
2. Click **Chat** – the assistant guides you through clarifying questions, frameworks, and calculations.  
3. Receive immediate feedback and a downloadable scorecard when you finish.

### Solve a Real Business Problem
1. Open the *Business Solution Bot*.  
2. Provide context, goals, constraints, and any prior attempts.  
3. Press **Analyse** to receive a strategic framework & actionable recommendations.
