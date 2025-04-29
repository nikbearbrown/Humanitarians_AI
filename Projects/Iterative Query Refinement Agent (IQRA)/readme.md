# 🤖 Iterative Query Refinement Agent

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=flat-square&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2.26.0%2B-green?style=flat-square&logo=requests&logoColor=white)
![Rich](https://img.shields.io/badge/Rich-Terminal%20Formatting-brightgreen?style=flat-square)
![JSON](https://img.shields.io/badge/JSON-Data%20Storage-lightgrey?style=flat-square)
![Wikipedia API](https://img.shields.io/badge/Wikipedia-OpenSearch-blue?style=flat-square)

Welcome to the **Iterative Query Refinement Agent** – your smart CLI companion that transforms rough queries into polished, context-rich questions and benchmarks refined answers against direct responses, all while logging a searchable history.

---

## 🚀 Key Features

- **Query Variation Generation**  
  Generates three distinct reformulations of your initial query to explore different angles.

- **Wikipedia Context Retrieval**  
  Automatically fetches concise background information for each variation via the Wikipedia OpenSearch API.

- **Insight Extraction**  
  Distills each variation’s LLM response into a single core fact or insight.

- **Final Answer Synthesis**  
  Combines distilled insights into a structured refined answer with an overview, bullet-point takeaways, and conclusion.

- **Direct Answer Comparison**  
  Retrieves a straightforward LLM response to your original query for side-by-side benchmarking.

- **Benchmark Analysis**  
  Compares refined vs. direct answers on processing time, word count, and source usage.

- **Persistent Memory**  
  Logs every query, variation, and response to `query_memory.json` for future reference.

- **Rich Terminal Interface**  
  Uses Rich library panels and tables for an engaging CLI experience.

---

## 🛠️ Tech Stack

- **Python 3.7+**  
- **requests** — LLM and Wikipedia API calls  
- **rich** — Enhanced terminal output  
- **Ollama API (model: llama3)** — Query generation & answering  
- **JSON** — Local memory persistence

---

## 📁 Repository Structure

```
iterative_query_refinement_agent/
├── agent.py             # Main class and CLI entrypoint
├── query_memory.json    # Stored history of queries & responses
└── README.md            # This documentation
```

---

## 🔧 Setting Up

1. **Install Dependencies**  
   ```bash
   pip install requests rich
   ```
2.  **Run Ollama API**  
   Make sure the Ollama server with the **llama3** model is running at:  
   `http://localhost:11434/api/generate`  
   To use a different endpoint or model, update the `_query_ollama` method in `agent.py`.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or later  
- Ollama API with the **llama3** model

### Installation

```bash
git clone https://github.com/your-username/iterative-query-refinement-agent.git
cd iterative-query-refinement-agent
```

---

## 🖥️ Usage

```bash
python agent.py
```

1. **Enter** your initial search query.  
2. **Observe** the agent as it:  
   - Generates query variations  
   - Retrieves Wikipedia context  
   - Executes LLM calls per variation  
   - Extracts core insights  
   - Synthesizes a refined answer  
   - Fetches a direct answer for comparison  
   - Performs benchmark analysis  
3. **Review** all entries in `query_memory.json`.

---

## 🧩 Example Use Cases

- **Academic Research**: Refine literature-review queries with richer context.  
- **Quick Fact-Checking**: Validate and compare distilled insights.  
- **Exploratory Analysis**: Discover different angles on business or technical questions.

---
## 🖥️ Example Output

Below is an example run refining the query **"what are eclipses?"**.

### Generated Query Variations

![Step 1: Generated Query Variations](images/Step1.png)

*Displays three reformulated queries exploring definition, frequency, and cause of eclipses.*

### Processing Variations

![Step 2: Processing Variations](images/Step2.png)

*Shows the Wikipedia context retrieval and LLM responses for each variation.*

### Key Insights Extraction

![Step 3: Key Insights](images/Step3.png)

*Extracts a single core insight from each LLM response.*

### Final Refined Answer

![Step 4: Refined Answer](images/Step4.png)

*Combines the extracted insights into an overview, bullet points, and a conclusion.*

### Direct Answer Comparison

![Step 5: Direct Answer](images/Step5.png)

*Presents the direct LLM answer for benchmark comparison.*

### Benchmarking Analysis

![Step 6: Benchmarking Analysis](images/Step6.png)

*Compares processing time, word count, sources used, and variations processed.*

---

## 🔮 Future Enhancements

- Support for additional knowledge sources (e.g., News API, academic databases).  
- Web-based interface using Streamlit or FastAPI.    
- Visualization of benchmarking metrics (charts & graphs).

## 📜 License

This project is licensed under the MIT License.

---

## 📧 Get in Touch

Got questions or feedback? Reach out:

- 📬 **Email:** [veenadharinishukla55@gmail.com](mailto:veenadharinishukla55@gmail.com)  
- 💼 **LinkedIn:** [linkedin.com/in/veenadharini-shukla](https://www.linkedin.com/in/veenadharini-shukla)  
- 👨‍💻 **GitHub:** [github.com/veenadharini](https://github.com/veenadharini)

Or, feel free to open an issue on the repo. Let’s refine queries smarter 🚀
