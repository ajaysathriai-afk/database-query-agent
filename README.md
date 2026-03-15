---

title: AI Database Query Agent
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: "4.16.0"
python_version: "3.11"
app_file: app.py
pinned: false
-------------

# AI Database Query Agent

An AI-powered data analytics assistant that converts natural language questions into SQL queries and visualizes the results.

## Features

* Natural language → SQL conversion using LangChain agents
* Automated data visualization with Plotly
* Interactive UI built with Gradio
* SQLite sample database
* Real-time AI reasoning logs

## Tech Stack

Python, LangChain, OpenAI, Gradio, SQLite, Plotly, Pandas

## Example Queries

* Show top 5 products by revenue
* List all customers from USA
* Which products generated the most sales?

## Architecture

User Question → AI SQL Agent → SQL Query → Database → DataFrame → Visualization → UI


# AI Database Query Agent

An AI-powered data analytics assistant that converts natural language questions into SQL queries and visualizes the results.

## Features

* Natural language → SQL conversion using LangChain agents
* Automated data visualization with Plotly
* Interactive UI built with Gradio
* SQLite sample database
* Real-time AI reasoning logs

## Tech Stack

* Python
* LangChain
* OpenAI
* Gradio
* SQLite
* Plotly
* Pandas

## Example Queries

* "Show top 5 products by revenue"
* "List all customers from USA"
* "Which products generated the most sales?"

## Architecture

User Question → AI SQL Agent → SQL Query → Database → DataFrame → Visualization → UI






# AI Database Query Agent

An AI-powered data assistant that converts natural language questions into SQL queries, executes them on a database, and returns both visualizations and results.

Built using **LangChain Agents, OpenAI LLMs, SQLite, Pandas, Plotly, and Gradio**.

---

## 🚀 Features

* Natural language → SQL conversion using AI
* Autonomous SQL agent using **LangChain**
* Automatic database schema exploration
* Data visualization (Bar, Line, Pie, Table)
* AI-generated explanations of query results
* Interactive web UI built with **Gradio**

---

## 🧠 Example Queries

* Show top 5 products by revenue
* What are the total sales?
* List all customers from USA
* Which product has highest sales?

---

## 🏗 System Architecture

User Question
↓
AI SQL Agent (LangChain + GPT)
↓
SQL Query Generation
↓
SQLite Database Execution
↓
Pandas Data Processing
↓
Plotly Visualization
↓
Gradio Web Interface

---

## ⚙️ Tech Stack

* Python
* LangChain
* OpenAI GPT
* SQLite
* Pandas
* Plotly
* Gradio

---

## 📊 Architecture Diagram

```
User
 │
 ▼
Gradio Web UI
 │
 ▼
LangChain SQL Agent
 │
 ▼
OpenAI GPT Model
 │
 ▼
SQL Query Generation
 │
 ▼
SQLite Database
 │
 ▼
Pandas DataFrame
 │
 ▼
Plotly Visualization
 │
 ▼
Results + Charts
```

---

## 🛠 Installation

```bash
git clone https://github.com/yourusername/database-query-agent.git

cd database-query-agent

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

Create `.env`

```
OPENAI_API_KEY=your_api_key_here
```

Run the application:

```
python app.py
```

---

## 💡 Example Output

The system automatically:

* Generates SQL queries
* Executes them on the database
* Visualizes results
* Provides AI explanations

---

## 📌 Future Improvements

* Multi-agent query planning
* Support for PostgreSQL / MySQL
* Automatic chart selection
* Query history and analytics

---

## 👨‍💻 Author

Ajay Kumar Sathri

AI / Machine Learning Engineer
