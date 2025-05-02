# 🧠 LLM-Powered Debate Agent

## Overview

The **Debate Agent** is an intelligent system designed to simulate structured debates on complex topics using Large Language Models (LLMs) via the Groq API. It automates the generation, evaluation, and synthesis of arguments from multiple perspectives—supportive, contrarian, and legal/ethical—and delivers a balanced judgment based on structured reasoning and scoring.

This tool is ideal for exploring nuanced viewpoints, enhancing critical thinking, and aiding in ethical decision-making and educational debates.

---

## 🚀 Key Features

- **Perspective Generation**: Automatically generates structured arguments from three diverse standpoints on any topic.
- **Evidence & Consistency Scoring**: Rates each perspective based on reliability of evidence, logical soundness, and ethical alignment.
- **LLM-Powered Judgment**: Synthesizes perspectives and provides a well-reasoned conclusion using Groq’s LLaMA 3 model.
- **JSON Storage**: Saves debate transcripts and outcomes to a local file for reference and tracking.
- **Rich Console Output**: Uses `rich` for clean, colorful, and step-by-step terminal output.

---

## 📁 Detailed File Structure

```
Debate-Agent/
│── debate_agent.py          # Core debate engine and Groq integration
│── procon_debates.json      # Stores generated debates and final judgments
│── .env                     # Environment file for secure API keys
│── requirements.txt         # Python package dependencies
│── README.md                # Project documentation and usage guide
```

---

## 🧪 Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Add your Groq API key to `.env`

```
GROQ_API_KEY=your_api_key_here
```

### 3. Run the Debate Agent

```bash
python debate_agent.py
```

When prompted, enter a debate question (e.g., “Should AI be allowed to make legal decisions?”), and watch the agent simulate a full debate with reasoned perspectives and a conclusive judgment.

---

## 🧩 System Design

### Architectural Overview

The Debate Agent is structured as a single-agent loop that delegates reasoning steps to the Groq LLaMA-3 LLM. The system follows a structured workflow:

1. **Prompt Construction**: Builds detailed system prompts for multiple perspectives.
2. **Perspective Generation**: Calls the LLM to get stances and evaluate them.
3. **Judge Evaluation**: Compares the strengths and weaknesses across perspectives.
4. **Data Persistence**: Saves all outputs to a JSON file for traceability.

### Core Components

| Module                    | Responsibility                                                       |
|---------------------------|------------------------------------------------------------------------|
| `get_debate_prompt()`     | Generates tailored prompts for LLM to simulate different perspectives. |
| `get_judge_prompt()`      | Builds a structured prompt to judge all arguments fairly.              |
| `call_llm()`              | Handles Groq API calls with retries and rate limit handling.           |
| `run_debate()`            | Orchestrates the full end-to-end debate simulation.                    |

---

## 🛠️ Technology Stack

- **Python** – Core programming language
- **Groq API** – Access to LLaMA 3 for reasoning and natural language generation
- **Rich** – For enhanced CLI visual output
- **Dotenv** – For environment variable management
- **JSON** – For structured storage of debate outcomes

---

## 🗂 Workflow Diagram

```
User Input
    ↓
Generate Perspectives (3)
    ↓
Score Perspectives: Evidence, Logic, Ethics
    ↓
Judge Evaluation
    ↓
Final Verdict + Saved JSON Output
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Open a pull request.

Let’s improve critical thinking through AI—together!

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 📧 Get in Touch

Have questions, ideas, or feedback?

- 📬 **Email**: rastogineha864.com  
- 💼 **LinkedIn**: [linkedin.com/in/neharastogi31](https://linkedin.com/in/neharastogi31)  
- 👨‍💻 **GitHub**: [github.com/rastogi-neha](https://github.com/rastogi-neha)

Let’s build something amazing!

---
