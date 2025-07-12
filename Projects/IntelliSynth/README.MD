# 🧠 IntelliSynth: Autonomous Research Collaborator

## 📘 Project Summary

**IntelliSynth** is a collaborative AI system designed to tackle research-oriented queries by distributing tasks among intelligent digital agents. Each agent focuses on a distinct aspect of the problem—ranging from fact-gathering to analysis—and contributes to a unified, in-depth report. This makes IntelliSynth an ideal tool for analysts, students, and knowledge professionals who require efficient and structured research support.

---

## 🌟 Core Capabilities

- **Adaptive Topic Analysis**: Automatically identifies key components of a research question.
- **Agent-Based Task Allocation**: Assigns different responsibilities to specialized sub-agents.
- **Multimodel Processing**: Integrates both OpenAI and Claude APIs for diverse reasoning.
- **Knowledge Fusion**: Combines outputs from all agents to form a cohesive narrative.
- **Human-Readable Summaries**: Presents results in a clear, structured, and actionable format.
- **Console Insight Visuals**: Offers enhanced CLI feedback using `Rich` for transparent execution.

---

## 🗂 Project Layout

```
IntelliSynth/
├── core_engine.py           # Main logic for agent interactions
├── launcher.py              # CLI entry script
├── session_output.json      # Logs and results from agent responses
├── .env                     # Secure storage for API keys
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## ⚙️ Setup Instructions

1. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Add your API keys** in the `.env` file:

   ```env
   OPENAI_API_KEY=your_openai_key
   CLAUDE_API_KEY=your_claude_key
   ```

3. **Launch the application**:

   ```bash
   python launcher.py
   ```

4. **Input a research topic** to receive a comprehensive analysis report.

---

## 🧬 System Workflow

### 🔄 Operational Flow

The system operates through a sequence of coordinated agent tasks:

1. **Input Intake**: Accepts a broad research question.
2. **Decomposition Module**: Breaks the topic into sub-questions.
3. **Agent Orchestration**: Assigns each subtask to a dedicated AI agent.
4. **Independent Processing**: Each agent queries an LLM (OpenAI/Claude).
5. **Result Aggregation**: Synthesizes all outputs into a unified summary.

---

## 🔑 Modules Overview

- **Input Handler**: Manages user input and query pre-processing.
- **Task Splitter**: Analyzes and divides the topic into 3–5 actionable tasks.
- **Agent Fabricator**: Generates specific agent instances with tailored objectives.
- **Execution Core**: Routes subtasks to LLMs and handles agent lifecycle.
- **Synthesizer**: Merges responses into a final report with contextual linking.

---

## 🧰 Technology Stack

- **Python** – Core programming language
- **LangChain** – Agent management and LLM coordination
- **OpenAI & Claude APIs** – Natural language model backends
- **Rich** – CLI interface for execution logs
- **Dotenv** – Secure API key management

---

## 🔁 Visual Workflow

```
User Input
   ↓
Topic Breakdown
   ↓
Agent Assignment
   ↓
Task Execution via LLMs
   ↓
Results Merged
   ↓
Structured Output (Console + JSON)
```

---

## 👥 Contributing

We welcome contributions from developers, researchers, and AI enthusiasts:

1. Fork this repository
2. Create your feature branch:
   ```bash
   git checkout -b <branch-name>
   ```
3. Commit your changes:
   ```bash
   git commit -m "Commit comments"
   ```
4. Push to the branch:
   ```bash
   git push origin <branch-name>
   ```
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute it as per the license terms.

---
