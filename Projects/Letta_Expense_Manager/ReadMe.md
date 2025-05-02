# Letta-Expense-Manager

Letta Expense Manager is an AI-powered financial tracking app built using **Streamlit** and **Letta AI**. It helps users gain visibility into their expenses, track budgets, forecast future spending, and receive intelligent financial insights — all through an easy-to-use interface.

---

## 🚀 Features

### 🔍 Core Features
- Upload transaction data via CSV
- Automatic expense categorization
- Interactive charts and filters for spending analysis
- Integration with Letta AI for insights and tips

### 💡 Enhanced Features
- Set and track budget limits per category
- Detect recurring expenses and subscriptions
- Forecast future expenses based on trends
- Spot anomalies and potential duplicate transactions
- Advanced filters by amount, description, weekday, and more
- Export data as CSV, Excel, or JSON
- Set and monitor savings goals
- Get a personalized Financial Health Score
- Receive AI-driven financial recommendations

---

## 🧰 Prerequisites

Make sure you have the following installed:
- Python 3.7 or higher
- pip (Python package manager)

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/letta-expense-manager.git
cd letta-expense-manager
```

### 2. Create `requirements.txt`

```txt
streamlit>=1.10.0
pandas>=1.3.0
matplotlib>=3.4.0
numpy>=1.20.0
openpyxl>=3.0.9
letta_client
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Letta Setup

### 1. Install Letta CLI

```bash
pip install letta
```

### 2. Start Letta Server Locally

```bash
letta server --ade --port=8283
```

Make sure your app uses the URL `http://localhost:8283` to connect to Letta.

---

## 🖥️ Running the App

```bash
streamlit run app.py
```

---

## 📂 How to Use

### Upload Transactions
- Upload a CSV with at least three columns: `Date`, `Description`, and `Amount`
- You can also generate sample data using the sidebar option

### Analyze Expenses
- Visualize weekly spend across categories
- Filter by amount, date, weekday, and keywords
- Detect anomalies and recurring transactions

### Manage Budgets
- Set category-level budgets from the sidebar
- View progress bars and alerts for overspending

### Track Savings
- Define savings goals and view progress
- Letta helps estimate required savings rates

### Export & Share
- Export your data as `.csv`, `.xlsx`, or `.json`
- Email summaries by configuring SMTP credentials in the sidebar

### AI Insights
- Letta AI analyzes your spending and gives personalized tips
- Customize your Letta Agent ID and endpoint via sidebar settings

---

## 🔐 Configuration Notes

- Email functionality requires valid SMTP settings
- You can customize spending categories in the app
- Letta API credentials should be stored securely and entered via the sidebar

---


## 🎬 Working Demo Video

Demo video: https://share.synthesia.io/8354d7c9-fa71-47e7-8fdf-b7868e77c700

Check out the live demonstration of Letta Expense Manager in action! The video showcases:
- Setting up the application
- Importing and categorizing transaction data
- Exploring the interactive dashboard
- Using Letta AI for personalized financial insights
- Budget tracking and anomaly detection features

---

## 📫 Contact

If you encounter any issues or have feature requests, feel free to open an issue on the repository.

### 👤 Authors

Shreyas Dasari

LinkedIn: https://www.linkedin.com/in/shreyas-dasari

GitHub: https://github.com/ShreyasDasari


Soorya Vijayaragavan

LinkedIn: http://www.linkedin.com/in/soorya-v

GitHub: https://github.com/vsoorya98


Sampada Kasture

LinkedIn: https://www.linkedin.com/in/sampadakasture07

GitHub: https://github.com/sampada-kasture

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).


---

