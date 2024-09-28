import streamlit as st
from langchain_community.llms import Replicate
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
os.environ["REPLICATE_API_TOKEN"] = st.secrets["api"]["REPLICATE_API_TOKEN"]
# replicate_id = st.secrets["id"]["REPLICATE_ID"]

llama2_chat_replicate = Replicate(
    model="meta/llama-2-13b-chat", model_kwargs={"temperature": 0.02, "max_length": 700, "top_p": 1}
)

llm = llama2_chat_replicate

template = """Based on the table schema below, write a SQL query that would answer the user's question:
{schema}

Question: {question}
SQL Query:"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Given an input question, convert it to a SQL query. No preamble."),
        ("human", template),
    ]
)

st.set_page_config(
    page_title="SQL Gen",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'About': 'Hello'
    }
)

def main():
    st.title("SQL Gen")
    st.write("A simple tool to generate SQL queries")
    schema = st.text_area("Enter schema", key="schema")
    if schema:
        generate(schema)

def generate(schema):
    question = st.text_input("Enter your query", key="query")

    if st.button("Generate SQL"):
        if not question:
            st.error("Please enter question !!")
        else:
            with st.spinner("Please wait for a few seconds :)"):
                try:
                    input_data = {"schema": schema, "question": question}
                    sql_response = (
                        prompt
                        | llm.bind(stop=["\nSQLResult:"])
                        | StrOutputParser()
                    )
                    result = sql_response.invoke(input_data)
                    
                    st.success("SQL query generated successfully.")
                    st.code(result, language="sql")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    st.error(f"Details: {str(e)}")

    if st.button("RESET"):
        try:
            st.rerun()
        except Exception as e:
            st.error(f"An error occurred while resetting the page: {e}")

if __name__ == "__main__":
    main()
