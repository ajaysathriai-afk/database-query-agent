from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain.agents.agent_types import AgentType
import os
import re
import sys
from io import StringIO


class SQLQueryAgent:

    def __init__(self, db_uri):

        print("🔧 Initializing SQL Agent...")

        self.db = SQLDatabase.from_uri(db_uri)

        print("🤖 Connecting to GPT...")

        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0
        )

        print("⚙️ Creating LangChain SQL Agent...")

        self.agent = create_sql_agent(
            llm=self.llm,
            db=self.db,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True
        )

        print("✅ Agent ready!\n")

    def extract_sql(self, logs):

        # pattern 1: Action Input
        match = re.search(r'Action Input:\s*"(SELECT .*?)"', logs, re.DOTALL | re.IGNORECASE)

        if match:
            return match.group(1)

        # pattern 2: raw SQL block
        match = re.search(r'(SELECT .*?;)', logs, re.DOTALL | re.IGNORECASE)

        if match:
            return match.group(1)

        return None

    def query(self, question):

        print("============================================================")
        print(f"💬 USER QUESTION: {question}")
        print("============================================================\n")

        # capture agent logs
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()

        result = self.agent.invoke({"input": question})

        sys.stdout = old_stdout

        logs = mystdout.getvalue()

        # print logs again so you still see them in terminal
        print(logs)

        answer = result.get("output", "")

        sql_query = self.extract_sql(logs)

        return answer, sql_query

    def get_schema(self):
        return self.db.get_table_info()