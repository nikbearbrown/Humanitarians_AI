# 🧠 Smart Database System using MCP

This project is a **Modular Smart Database System** built with **MCP (Modular Command Protocol)**. It allows users to interact with databases using modular plugins and optional natural language capabilities. Ideal for data analysis, interactive exploration, and intelligent query execution.

---

## 🔧 Features

- 📦 **MCP-based Plugin Architecture** — Easily extend functionality
- 🗃️ **SQLite / PostgreSQL support**
- 🧠 **Natural Language to SQL Conversion** (optional LLM integration)
- 📊 **Data summarization & visualization**
- 🧾 **CSV Import/Export** with type inference
- 🧰 **Interactive CLI Interface**
- 🔐 **Command History and Logging**

---

## 📁 Project Structure

smart-db-mcp/
│
├── mcp/ # Core MCP system
│ ├── base_plugin.py # Defines plugin interface
│ └── mcp_router.py # Routes commands to plugins
│
├── plugins/ # Plugin modules
│ ├── sql_engine.py # Executes SQL queries
│ ├── csv_importer.py # Imports CSVs to database
│ ├── nl_to_sql.py # Optional: Natural language to SQL (LLM)
│ ├── data_viz.py # Data plotting/stats
│
├── data/ # Sample CSVs and databases
│
├── main.py # CLI entry point
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourname/smart-db-mcp.git
cd smart-db-mcp
2. Install Requirements
bash

pip install -r requirements.txt
3. Run the CLI Interface

bash

python main.py
🧩 Example Commands

shell

> import_csv data/employees.csv as employees
> summarize employees
> plot age, salary from employees
> query "Show me the average salary by department"
> query SELECT * FROM employees WHERE age > 30;
🧠 Optional: Enable Natural Language Queries
Set your environment variable (if using OpenAI):

bash

export ENABLE_NL2SQL=True
export OPENAI_API_KEY=your-api-key-here
Then, try:

shell

> query "List all sales from last month over $10,000"

✨ Plugin Architecture
Each plugin inherits from a base interface:

python
Copy
Edit
class Plugin:
    def can_handle(self, command: str) -> bool:
        ...
    def handle(self, command: str) -> str:
        ...
Plugins are automatically discovered and routed by mcp_router.py.

🛠 Requirements
Python 3.8+

SQLite3 or PostgreSQL

Optional: OpenAI API key for NL2SQL

📜 License
This project is licensed under the MIT License.


