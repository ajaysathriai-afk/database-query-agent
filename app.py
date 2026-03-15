import gradio as gr
from dotenv import load_dotenv
import os

from core.database import DatabaseManager
from core.sql_agent import SQLQueryAgent
from core.visualizer import DataVisualizer

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found")

print("🚀 Starting Database Query Agent")

db_manager = DatabaseManager()
agent = SQLQueryAgent(db_manager.get_connection_string())
visualizer = DataVisualizer()


def process_query(question, chart_type):

    if not question.strip():
        return "Please enter a question", None, ""

    try:

        print("\n" + "=" * 60)
        print("💬 USER QUESTION:", question)
        print("=" * 60)

        answer, sql_query = agent.query(question)

        chart = None

        if sql_query:

            df = db_manager.execute_query(sql_query)

            if df is not None and not df.empty:

                chart = visualizer.create_chart(df, chart_type)

        return answer, chart, sql_query

    except Exception as e:

        return f"Error: {str(e)}", None, ""


def show_schema():
    return agent.get_schema()


css = """

body{
background:#020617;
font-family:Inter,system-ui;
}

#title{
text-align:center;
font-size:40px;
font-weight:800;
color:#e2e8f0;
margin-bottom:20px;
}

.query-box{
background:#0f172a;
color:white !important;
padding:20px;
border-radius:12px;
border:1px solid #334155;
font-size:16px;
line-height:1.6;
}

.query-box *{
color:white !important;
}

button{
background:linear-gradient(90deg,#6366f1,#8b5cf6) !important;
color:white !important;
border-radius:10px !important;
font-weight:600 !important;
}

"""


with gr.Blocks() as app:

    gr.Markdown("# 🗄️ Database Query Agent", elem_id="title")
    gr.Markdown("Ask questions in plain English — AI converts them into SQL!")

    with gr.Row():

        with gr.Column(scale=1):

            gr.Markdown("### Ask a Question")

            question = gr.Textbox(
                label="Your Question",
                placeholder="Show top 5 products by revenue",
                lines=3
            )

            chart_type = gr.Radio(
                choices=["table", "bar", "line", "pie"],
                value="table",
                label="Visualization Type"
            )

            query_btn = gr.Button("🔍 Query Database")

            gr.Markdown("### Example Questions")

            ex1 = gr.Button("What are the total sales?")
            ex2 = gr.Button("Show top 5 products by revenue")
            ex3 = gr.Button("List all customers from USA")
            ex4 = gr.Button("Which product has highest sales?")

            schema_btn = gr.Button("📋 Show Database Schema")

        with gr.Column(scale=2):

            gr.Markdown("### 🤖 AI Response")

            answer_box = gr.Markdown(elem_classes="query-box")

            gr.Markdown("### 📊 Visualization")

            chart_box = gr.Plot()

            gr.Markdown("### 💻 Generated SQL")

            sql_box = gr.Code()

    query_btn.click(
        process_query,
        inputs=[question, chart_type],
        outputs=[answer_box, chart_box, sql_box]
    )

    ex1.click(lambda: "What are the total sales?", None, question)
    ex2.click(lambda: "Show top 5 products by revenue", None, question)
    ex3.click(lambda: "List all customers from USA", None, question)
    ex4.click(lambda: "Which product has highest sales?", None, question)

    schema_btn.click(show_schema, None, answer_box)


app.launch()