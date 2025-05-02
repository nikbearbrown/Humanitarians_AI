🧠 Smart Database System using MCP (Model Context Protocol)
This project is a Modular Smart Database System powered by the Model Context Protocol (MCP) — a lightweight, extensible protocol for routing commands to specialized data-handling modules. It supports SQL engines, CSV import/export, data visualization, and optional natural language query processing via LLMs.

🔧 Features
🔌 MCP (Model Context Protocol) — Dynamic plugin-based command routing

🗃️ Supports SQLite & PostgreSQL backends

🧠 Natural Language to SQL (optional via OpenAI or similar LLMs)

📈 Data summarization & visualization for quick insights

📄 CSV Import/Export with smart type inference

💬 Interactive CLI Interface with command history & logging

🔍 Pluggable architecture for scalable extensibility

📁 Project Structure

smart-db-mcp/
├── mcp/                # Core Model Context Protocol engine
│   ├── base_plugin.py  # Plugin base class and interface
│   └── mcp_router.py   # Core command dispatcher using MCP
│
├── plugins/            # Command-specific handler modules
│   ├── sql_engine.py     # SQL execution
│   ├── csv_importer.py   # CSV to DB import
│   ├── nl_to_sql.py      # Optional: LLM-based NL to SQL
│   └── data_viz.py       # Statistical analysis & plotting
│
├── data/              # Sample databases and CSV files
├── main.py            # CLI entry point
├── requirements.txt   # Dependencies
└── README.md          # Project documentation
🚀 Getting Started
1. Clone the Repository

git clone https://github.com/yourname/smart-db-mcp.git
cd smart-db-mcp
2. Install Requirements

pip install -r requirements.txt

3. Run the CLI

python main.py

🧪 Example Commands

> import_csv data/employees.csv as employees
> summarize employees
> plot age, salary from employees
> query "Show me the average salary by department"
> query SELECT * FROM employees WHERE age > 30;

🧠 Optional: Natural Language Query Support
To enable NL to SQL conversion, set the following environment variables:

export ENABLE_NL2SQL=True
export OPENAI_API_KEY=your-api-key-here
Try this:

> query "List all sales from last month over $10,000"
🔌 Plugin Architecture (via MCP)
All plugins must inherit from the base interface and implement two methods:

class Plugin:
    def can_handle(self, command: str) -> bool:
        ...
    def handle(self, command: str) -> str:
        ...
Plugins are auto-discovered and routed through mcp_router.py, which enables seamless expansion.

🛠 Requirements
Python 3.8+

SQLite or PostgreSQL

(Optional) OpenAI API key for LLM-based queries

📜 License
Licensed under the MIT License.

